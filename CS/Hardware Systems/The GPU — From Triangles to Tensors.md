---
chinese: 图形处理器：从三角形到张量 (túxíng chǔlǐqì)
prerequisites:
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Matrix]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/computer-architecture
  - domain/parallel-computing
  - level/A-Level
  - level/university
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/9618-15-1
  - syllabus/IB-CS-A1-1
  - syllabus/IB-CS-A4-1
  - type/deep
  - misconception/gpu-is-a-faster-cpu
  - misconception/cores-are-comparable
  - misconception/peak-flops-is-performance
---

# The GPU — From Triangles to Tensors 图形处理器：从三角形到张量

## Definition — the picture is millions of small jobs

Turn the camera in a game. The screen must be rebuilt: move the vertices of the world into the camera's view, decide which surfaces cover each sample, and work out their colours. At 1920×1080 and 60 frames per second, the display contains **124,416,000 pixel positions per second**. That is a count of displayed positions, not shader invocations: overlap, multiple passes and antialiasing change the actual work.

A **graphics processing unit (GPU)** is a processor designed to achieve high throughput across many parallel operations, originally for graphics. Its programmable execution units also run **compute kernels**—functions applied to many work items without requiring a picture as output.

The important question is not “which chip is faster?” It is **“what can happen independently, and how much data must move to make it happen?”**

A CPU is good at making progress through a complicated stream of decisions. A GPU devotes much of its machinery to keeping many arithmetic lanes busy. Both use parallelism and caches; their balance differs. They usually cooperate within the same system.

### 中文锚点

玩游戏时，你转一下视角，整张画面就得重新算。可屏幕上相邻的一大片位置，往往都在问很相似的问题：“这里属于哪个表面？光照上去是什么颜色？”这就像给全班合照统一调亮：每个位置的数据不同，却可以照着同一套步骤一起处理。GPU 擅长把这种成片的活摊开做；如果每一步都得等上一步的答案，人再多也帮不上忙。关键不只是有多少人在算，而是这些活能不能同时开工。

## 1. A triangle becomes a picture

A mesh represents a surface using vertices and connections, often triangles. Each vertex can carry position, colour, a surface normal and texture coordinates. A **texture** is sampled data—often an image—used by a shader; it is not the final framebuffer.

A simplified rasterisation pipeline is:

1. **Vertex processing.** Transform each vertex from object coordinates through the camera and projection. In homogeneous coordinates, $p_{clip}=PVMp$, where $M,V,P$ are model, view and projection matrices. Clipping removes geometry outside the viewing region; division by the homogeneous $w$ produces normalised coordinates, then a viewport maps them to the screen.
2. **Rasterisation.** Determine which sample positions a triangle covers. Generate candidate **fragments**, carrying interpolated attributes.
3. **Fragment shading.** Run a program that computes colour or other outputs, using material, texture and lighting data.
4. **Visibility and combination.** Depth/stencil tests and blending determine how candidates contribute to framebuffer samples. Implementations may perform eligible depth tests early. Resolve multisampling if needed, then present the image.

A fragment is **not a guaranteed final pixel**. Several triangles may produce candidates for the same location; hidden ones can fail a depth test. Transparency may combine colours instead of choosing one. [Khronos rendering pipeline](https://wikis.khronos.org/opengl/Portal%3ARendering_Pipeline).

### The interpolation has mathematics inside it

For a point inside a flat screen-space triangle with vertices $A,B,C$, find **barycentric weights**:

$$p=\lambda_A A+\lambda_B B+\lambda_C C,\qquad
\lambda_A+\lambda_B+\lambda_C=1,\qquad \lambda_i\ge0.$$

Why does this help? The weights describe the point as a mixture of the corners. Use the same mixture to interpolate a colour: $c(p)=\lambda_Ac_A+\lambda_Bc_B+\lambda_Cc_C$.

For $A=(1,1)$, $B=(7,1)$, $C=(1,7)$ and $p=(2.5,2.5)$, the vertical and horizontal offsets give $\lambda_B=\lambda_C=1.5/6=1/4$, leaving $\lambda_A=1/2$. Red, green and blue corner values mix into $(1/2,1/4,1/4)$.

![[gpu-rasterisation.svg|700]]

*One screen-space triangle; dots mark covered sample centres. The highlighted sample gets its colour from three weights. This toy uses one sample per pixel and no perspective.*

With perspective, linearly interpolating texture coordinates in screen space generally distorts them. For a smooth attribute $u$ with vertex values $u_i$ and clip coordinates $w_i$, use

$$u(p)=\frac{\sum_i\lambda_i u_i/w_i}{\sum_i\lambda_i/w_i}.$$

Interpolate $u/w$ and $1/w$, then divide. The ordinary weighted average is recovered when all $w_i$ are equal. This is why a receding tiled floor can keep its texture attached to the floor rather than sliding across it.

**Rasterisation and ray tracing ask different geometric questions.** Rasterisation starts from a primitive and finds its covered samples. Ray tracing starts from a ray and asks what it intersects. Modern renderers can mix them; specialised ray-intersection hardware is not the same as matrix hardware.

## 2. How a graphics pipeline became programmable

The change happened in stages, not in one miraculous invention:

| Stage | What the programmer gains |
|---|---|
| Fixed-function graphics | Configure predefined transformations, lighting and texturing |
| Programmable shaders | Write the per-vertex or per-fragment calculation |
| Unified shader hardware | Schedule different shader stages on a shared pool of execution resources |
| General-purpose compute | Launch calculations directly, without encoding the problem as a drawing command |
| Specialised matrix units | Accelerate supported blocks of multiply-and-accumulate work |

Early GPGPU work encoded numerical arrays as textures and computed through graphics APIs. CUDA's public arrival in 2007 made general-purpose programming an explicit route on NVIDIA hardware. CUDA is one ecosystem; it is not the definition of a GPU. Other platforms expose computation through APIs such as Metal, Vulkan compute and HIP. [2007 NVIDIA GPU architecture paper](https://research.nvidia.com/sites/default/files/pubs/2007-02_How-GPUs-Work/04085637.pdf) · [CUDA at SIGGRAPH 2007](https://www.nvidia.com/content/events/siggraph_2007/supercomputing.html).

The historical consequence is told in [[You Never Expect the Change of Needs]] §Cultural ripples: a capability built for one market became useful elsewhere. The technical bridge is **repeated arithmetic on arrays**, not the claim that every AI operation is literally a graphics operation.

## 3. SIMT: one program, many threads

A **thread** is one logical execution of the kernel, with its own index and local state. For an elementwise operation, thread $i$ might calculate $y_i=2x_i+1$. The program is shared; the values differ.

NVIDIA calls its programming/execution model **SIMT**: single instruction, multiple threads. Threads are grouped into **warps of 32**. A warp instruction acts on its active threads; different warps can be at different instructions. AMD uses wavefront terminology, with widths depending on architecture and mode. Do not turn one vendor's width into a law of all GPUs.

The useful hierarchy is:

| Level | Role |
|---|---|
| Grid | All thread blocks launched for a kernel |
| Block | Threads that can cooperate using block-local shared memory and barriers |
| Warp | A hardware-scheduled group of threads within a block |
| Streaming multiprocessor (SM) | NVIDIA's hardware unit that hosts resident blocks/warps and execution resources |
| Whole GPU | Many such units, caches, memory interfaces and often specialised engines |

Blocks need not run in a predictable order. Do not write an ordinary kernel that requires all its blocks to be resident simultaneously. Cross-block dependencies usually need another launch or an explicitly supported coordination mechanism.

**SIMD and SIMT are related, not interchangeable descriptions.** SIMD describes an instruction acting on multiple data elements; SIMT exposes individual threads and lets hardware group their execution. A whole GPU contains independently scheduled groups, so labelling the entire chip “one instruction stream” hides a level of its organisation.

### Branch divergence: what happens to the other lanes?

Suppose eight illustrated lanes reach:

```python
result = [x*x if x >= 0 else -x for x in values]
```

Some require a square; others require negation. In a simple masked-execution model, issue the square path with only its lanes active, then the negation path with the other lanes active. Work is still correct; available lane slots go unused on each path.

If four lanes take each equal-cost path, eight useful lane-operations occupy sixteen issued lane slots: **50% utilisation in this toy model**. Real cost depends on path lengths, predication, scheduling and other ready work. It is not automatically a 2× slowdown of the application.

Modern NVIDIA architectures maintain per-thread execution state and support independent thread scheduling. A warp is **not permission to omit synchronisation**. If one thread must consume another's write, use the required barrier and memory-ordering rules. A block barrier also must not be placed where only some required participants reach it. [NVIDIA SIMT and scheduling](https://docs.nvidia.com/cuda/cuda-programming-guide/03-advanced/advanced-kernel-programming.html).

### Waiting does not stop the whole chip

When a warp waits for memory, the scheduler may issue a ready warp. This **hides latency** by doing other work; it does not make the memory request itself faster. Enough independent work must exist, and registers/shared-memory capacity limit how many warps can reside at once.

**Occupancy** measures resident warps relative to the hardware limit. Higher occupancy can help hide latency, but maximising it is not the goal at any cost: giving each block useful data reuse may consume shared memory while reducing expensive traffic.

## 4. The memory problem: feed the arithmetic

Recall that registers, caches and main memory differ in both capacity and access cost; [[RAM and the Memory Hierarchy]] develops that trade-off.

| Storage | Typical role and scope |
|---|---|
| Registers | A thread's live values; scarce capacity can limit residency or cause spills |
| Shared memory | Programmer-managed storage shared by a block; useful for cooperation and reuse |
| Caches | Hardware-managed reuse, with details depending on the architecture |
| Device/global memory | Large working arrays; a logical memory space, not “one equally cheap access” |
| Host memory | CPU-side data; discrete devices may need transfers before GPU use |

CUDA **local memory** is thread-private in meaning, but can reside in device memory. “Local” does not promise “register-fast.” Shared memory is block-local scratch storage; it is not the same thing as a CPU and integrated GPU sharing system RAM.

### Coalescing: neighbours should ask for neighbouring data

If neighbouring lanes load neighbouring array elements, hardware can often serve them with fewer memory transactions. If their requests are scattered, more transactions may be required for the same useful bytes. Alignment and access size matter. This is **coalescing**: combine compatible accesses, not magically merge unrelated addresses.

### Tiling: bring a useful patch close, then reuse it

For square matrices, the usual multiplication is

$$C_{ij}=\sum_{k=0}^{N-1}A_{ik}B_{kj}.$$

There are $N^2$ output entries, each with $N$ multiply-add steps: roughly $2N^3$ floating-point operations, counting one multiplication and one addition separately.

A naive no-cache model loads two input values for every multiply-add: $2N^3$ input elements. But neighbouring outputs reuse the same inputs. Organise one output tile of size $T\times T$:

1. Load a $T\times T$ tile of $A$ and one of $B$.
2. Cooperating threads wait until the shared tiles are ready.
3. Use their $2T^2$ values for $T^3$ multiply-add steps, accumulating output values.
4. Ensure readers have finished before overwriting the shared tiles; advance along $k$.

Each loaded $A$ value serves $T$ output columns; each loaded $B$ value serves $T$ output rows. **The saving is reuse, not fewer mathematical products.** [CUDA best practices: shared-memory matrix multiplication](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#shared-memory-in-matrix-multiplication-c-ab).

![[gpu-tiling.svg|700]]

*For this $2\times2$ tile step, eight input values supply eight multiply-adds. Repeating the same dot products independently would request sixteen input values in the deliberately cache-free model.*

![[gpu-work-and-reuse.mp4]]

*Follow the triangle's samples, watch divergent lanes become inactive, then see a pair of input tiles reused across an output tile. Lane counts and time are illustrative; this is an explanatory model, not a hardware trace.*

### Arithmetic intensity and the roofline

**Arithmetic intensity** $I$ is work per byte moved across a specified memory boundary. Always name the boundary; “bytes moved” is not one universal quantity.

In a tile step with float32 inputs, the idealised work is $2T^3$ FLOPs and the input traffic is $2T^2\times4$ bytes:

$$I_{input}\approx\frac{2T^3}{8T^2}=\frac T4\quad\text{FLOPs per byte}.$$

This local estimate excludes output traffic, caching effects and overhead. Increasing $T$ raises reuse, until resource limits and implementation details intervene.

If sustainable bandwidth is $B$ bytes/s and the relevant peak arithmetic rate is $P$, then

$$\boxed{\text{throughput}\ \lesssim\ \min(P,BI).}$$

Why? Arithmetic cannot exceed the execution machinery's capacity, and each incoming byte supports only $I$ operations. Choose the smaller ceiling. [[The True IO Bound]] uses this **roofline** viewpoint; a workload can be bandwidth-bound or compute-bound, and an optimisation can move the bottleneck.

## 5. From dot products to tensor cores

A dense neural-network layer repeatedly forms weighted sums. For a batch of inputs, these sums become matrix multiplication: $Y=XW+b$, followed by a nonlinearity. Images, speech and text produce different arrays, but large parts of their models share this arithmetic; [[Artificial Intelligence]] derives the neuron and learning process.

A **tensor** in these programming libraries is an array with a shape: a vector has one axis, a matrix two, a batch of colour images might have four. The term does not mean “a new kind of number.” Its use in mathematical geometry carries additional transformation structure.

A **tensor core** is NVIDIA's name for specialised hardware accelerating supported matrix multiply-and-accumulate operations, conceptually

$$D=AB+C.$$

For example, the 2017 Volta design performs a small $4\times4$ matrix operation with FP16 inputs and FP16/FP32 accumulation options; software combines such work into larger tiles. Later designs support other shapes and formats. A GPU's ordinary programmable arithmetic, matrix units and ray-tracing units perform different jobs. [Volta architecture, pp.15–16](https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf).

### Precision is a resource, not a free upgrade

Lower-precision inputs use fewer bits and can enable greater throughput and lower memory traffic. Wider accumulation reduces some accumulation error, but it **cannot restore information already lost when inputs were rounded**. FP16, BF16, float32 and quantised integers have different ranges, precision and scaling rules; see [[Floating-Point Representation]].

This is why a precision choice must be checked against the task: acceptable image classification accuracy, stable training, or a scientific error tolerance. “More TOPS” without the format, sparsity assumptions and workload is not a useful comparison.

Training stores activations and computes gradients; optimisers may keep additional parameter state. Inference omits back-propagation, but model weights, intermediate values and—for autoregressive language models—cached attention keys/values still occupy memory. Small batches and repeated weight reads can make inference bandwidth-sensitive; large matrix batches may better exploit arithmetic capacity. Neither stage has one permanent bottleneck.

## 6. The CPU and GPU are partners

A discrete-device calculation often follows this dependency chain:

**CPU prepares data → transfer inputs → enqueue kernel → wait for required results → transfer/read output.**

Launches can be asynchronous: returning from the launch does not imply completion. To time the work, measure the intended interval with appropriate synchronisation or device timing events. Otherwise a benchmark may time only the act of submitting a job.

Transfers and computation can sometimes overlap with suitable hardware, buffers and independent work. But if the next stage needs a particular result, that dependency remains. Integrated GPUs may share physical system memory with the CPU, avoiding some explicit copies; sharing memory does not eliminate bandwidth contention, synchronisation or coherence costs.

| Question | CPU usually favoured | GPU often favoured |
|---|---|---|
| How much independent work? | Small or strongly sequential job | Large batches of similar operations |
| What is the control flow? | Irregular decisions, pointer chasing | Work that keeps groups of lanes useful |
| Where are the data? | Already CPU-resident; transfer dominates | Already device-resident, or substantial reuse after transfer |
| What matters? | Fast response for one task | High throughput for many tasks |

These are workload tendencies, not universal speed rankings. GPUs can process irregular algorithms, and CPUs have vector instructions. Compare **end-to-end time, memory capacity, numerical quality and energy per completed task**, not advertised core counts.

A GPU can spend less energy per useful arithmetic operation when many lanes share instruction handling and loaded data. That advantage is workload-dependent: transfers, unused lanes and insufficient work can outweigh it. Higher chip power does not necessarily mean higher energy per completed job; energy is power integrated over the run.

**Simulation supplies another route from pictures to computation.** In a grid-based fluid model, many cells apply the same update rules to different local values. A GPU can process cells in parallel, then coordinate between time steps because each update depends on neighbouring states. The array structure fits; the dependencies still matter.

### Hardware choices for machine learning

Start with the task's data size, model state, latency, privacy, power and scaling needs:

| Scenario / hardware | Why it can fit—and what to check |
|---|---|
| Laptop CPU | Small tabular models, preparation, experiments; enough RAM and storage may matter more than an accelerator |
| GPU workstation | Repeated large tensor operations; check device memory, software support and transfer costs |
| Edge device | Run near a camera, phone or sensor for latency/privacy/offline operation; constrained power and memory may require a smaller model |
| ASIC / TPU | An application-specific integrated circuit fixes hardware for a class of work; Google's TPU family targets tensor computation. Efficiency comes with supported-operation and platform constraints |
| FPGA | Reconfigurable logic can implement a tailored streaming computation; flexibility differs from writing a CPU/GPU program and development effort matters |
| Cloud platform | Rent CPUs/accelerators/storage and scale capacity; include data movement, recurring cost, location and access constraints |
| HPC centre | Many compute nodes and fast interconnects tackle large training/simulation jobs; distributing work adds communication and coordination |

A TPU is a kind of ASIC, an edge device is a deployment location, and a cloud/HPC system contains processors: **these categories overlap**. Storage capacity holds the dataset; storage throughput feeds it; working/device memory holds the live computation. Adding accelerators does not fix a data loader or interconnect that cannot keep them supplied.

## Worked examples — choose the mechanism

### 1. Why graphics benefits — an actual exam prompt

OCR H446/01's sample assessment asks why a GPU is more effective than a CPU for graphics processing (Q8(c), three marks).

**Trigger:** similar transformations or shading calculations across many data items. **Tool:** data parallelism. A GPU can apply the relevant calculation across many vertices or fragments concurrently, so suitable graphics work completes at higher throughput. State the **workload → architectural feature → consequence** chain; merely expanding “GPU” does not explain the benefit. This follows the published marking guidance without claiming a GPU wins every computation. [OCR sample paper and mark scheme](https://www.ocr.org.uk/Images/170852-unit-h446-1-computer-systems-sample-assessment-materials.pdf).

### 2. A faster kernel that loses overall — original example

A CPU task takes 12 ms. A discrete GPU needs 5 ms to send the input, 3 ms to compute, and 5 ms to return the result; assume these dependent steps do not overlap.

**Trigger:** compare the user's completed job. **Tool:** add sequential stage times. The GPU route takes $5+3+5=13$ ms, slower than 12 ms. If ten independent iterations can keep their state on the device, the comparison becomes $5+10(3)+5=40$ ms against $10(12)=120$ ms. Check that each iteration really needs no CPU-side intermediate decision before claiming the reuse.

### 3. Reuse changes the ceiling — original example

A hypothetical accelerator sustains 200 GB/s across the selected memory boundary and has a relevant arithmetic ceiling of 4 TFLOP/s. A kernel has measured intensity 2 FLOPs/byte.

**Trigger:** memory supply may limit arithmetic. **Tool:** roofline bound. $BI=200\times10^9\times2=0.4\times10^{12}$ FLOP/s, so the ceiling is 0.4 TFLOP/s. If reuse raises intensity to 16, the bandwidth ceiling becomes 3.2 TFLOP/s. This gives headroom; it does not promise an eightfold measured speed-up. Other bottlenecks and overheads may bind.

## Hands-on — draw it, then count its work

The accompanying `gpu-lab.py` uses Python's standard library. Run `python3 gpu-lab.py` to:

- Rasterise the illustrated triangle into an SVG, inspecting barycentric weights and coverage.
- Execute scalar and tiled matrix multiplication and compare every output.
- Count modelled input loads while changing the tile size.
- Display active masks for a divergent group.

It executes on the CPU and models GPU ideas; it is **not a CUDA implementation or a GPU speed benchmark**. Real GPUs have caches and transaction rules omitted from the load counter. The Python tile version may be slower while requesting fewer modelled loads; interpreter overhead and hardware execution are different questions.

Here is the dot product at the centre of the calculation:

```python
def matmul(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    assert all(len(row) == inner for row in a)
    out = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                out[i][j] += a[i][k] * b[k][j]
    return out

assert matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
```

Predict before running: doubling the tile width should reduce modelled input loads for a square multiplication that divides evenly into tiles. Does it change the answer or the number of multiply-adds? What happens at a partial tile on the edge?

## Common misconceptions

- **“A GPU core is a small CPU core.”** Marketing counts can refer to arithmetic lanes; they do not measure equivalent independent processors.
- **“All threads run at once.”** Work is scheduled in groups; finite resources limit residency, and resident is not the same as currently executing.
- **“Every branch is disastrous.”** Uniform branches need not diverge. Divergence cost depends on paths and the surrounding workload.
- **“Shared memory removes the need to synchronise.”** Sharing creates dependencies; barriers/order make them safe.
- **“Tensor cores understand tensors or intelligence.”** They accelerate numerical operations. Meaning comes from the model and how it is used.
- **“A better GPU always raises game frame rate.”** The limiting work may be on the CPU, or elsewhere in the rendering chain.
- **“Peak arithmetic tells me the answer.”** Precision, data movement, utilisation and correctness all matter.

## Exam Notes

### IB Computer Science — first assessment 2027

**A1.1.2 (SL/HL)** requires GPU role, architecture and real-world uses, including games, AI and simulations. **A1.1.3 (HL only)** compares CPU/GPU design, cores, processing, memory access, energy efficiency and cooperation: task division, data sharing and coordinated execution. Give scenario-based explanations, not unqualified “GPU faster” slogans.

**A4.1.2 (SL/HL)** requires hardware configurations from laptops to advanced infrastructure, considering processing, storage and scalability; its named list includes ASICs, edge devices, FPGAs, GPUs, TPUs, cloud platforms and HPC centres. §6 supplies that comparison. A4.1.1 separately names deep, reinforcement, supervised, transfer and unsupervised learning; hardware knowledge does not replace that comparison. Barycentric formulae, CUDA-specific scheduling, tile arithmetic and Volta instruction shapes are explanatory enrichment, not named required algorithms.

### Cambridge 9618 and 0478

**9618 §15.1 (Paper 3)** requires SISD/SIMD/MISD/MIMD and massively parallel computers, alongside RISC/CISC and pipelining. GPU examples help explain parallel work; the specification does not name shader programming, CUDA or tensor-core implementation. [[Pipelining and Simultaneous Multithreading]] carries the taxonomy and pipeline foundations.

**0478 §3.1 (Paper 1)** teaches CPU operation and performance factors. The detailed GPU architecture and graphics pipeline here are enrichment, not a separately specified GPU outcome.

### OCR and AQA A Level

**OCR H446 §1.1.2(b)** explicitly requires GPUs and their uses, including non-graphics applications; §1.1.2(c) includes multicore and parallel systems. The sample question above shows the explanation style. **AQA 7517** covers processor components and performance in §4.7.3; it does not prescribe this GPU/shader/tensor-core treatment. Do not transfer OCR's explicit GPU wording into AQA's specification.

### AP and scope boundaries

**AP CSA (Fall 2025 CED)** does not prescribe processor architecture, GPU programming or the graphics pipeline. **AP CSP Topic 4.3** treats parallel/distributed computing and speed-up at a conceptual level; it does not require CUDA, shader stages or tensor-core internals. GPU libraries may implement a program's work, but that does not make their implementation an AP CSA learning objective. [AP CSA CED](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-a-course-and-exam-description.pdf) · [AP CSP CED](https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-course-and-exam-description.pdf).

## Connections

- **Parents:** [[Pipelining and Simultaneous Multithreading]] — overlap and ready work; [[RAM and the Memory Hierarchy]] — locality and storage costs; [[Matrix]] — the multiplication being accelerated.
- **Applications:** [[Artificial Intelligence]] — weighted sums and learning; [[Image Encoding]] — pixels and representations; [[Parallel and External Sorting]] — parallelism and its limits.
- **Precision:** [[Floating-Point Representation]] — format, range, rounding and error.
- **Meta:** [[The True IO Bound]] — computation waiting for data; [[Decouple and Recouple]] — queues and buffers separating rates.
- **Story:** [[You Never Expect the Change of Needs]] — capability outgrows the need that originally justified it.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $p=\sum_i\lambda_i p_i$ | `p=\sum_i\lambda_i p_i` | barycentric position |
| $C_{ij}=\sum_k A_{ik}B_{kj}$ | `C_{ij}=\sum_k A_{ik}B_{kj}` | matrix product |
| $D=AB+C$ | `D=AB+C` | matrix multiply-accumulate |
| $\min(P,BI)$ | `\min(P,BI)` | arithmetic / bandwidth ceiling |
