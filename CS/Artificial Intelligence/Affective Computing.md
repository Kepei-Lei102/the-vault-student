---
chinese: 情感计算 (qínggǎn jìsuàn)
aliases:
  - Emotion Recognition
  - Emotion AI
  - Sentiment Analysis
prerequisites:
  - "[[Artificial Intelligence]]"
  - "[[Privacy-Preserving Computation]]"
  - "[[Data Protection and Privacy]]"
  - "[[Conditional Probability]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/artificial-intelligence
  - domain/ethics
  - level/university
  - level/enrichment
  - curriculum/IB-CS
  - type/deep
  - misconception/expression-equals-emotion
  - misconception/accurate-detector-accurate-inference
  - misconception/more-data-fixes-bias
  - misconception/on-device-means-harmless
---

# Affective Computing 情感计算

> *In the late 2000s a student in Rosalind Picard's laboratory at MIT borrowed two of the lab's wristbands, which measure the tiny changes in skin conductance that come with excitement, for his little brother, who was autistic and could not say how he felt. Looking through the recordings later, Picard found that on one day the signal from one wrist had shot up higher than anything she had ever seen, while the other wrist stayed flat. She assumed the sensor was broken. It was not. Twenty minutes after that peak the boy had a grand mal seizure. The sensor had picked up an electrical storm deep in one side of his brain before anyone could see anything wrong. The wristband that grew out of that afternoon was cleared by the US Food and Drug Administration in 2018 to call for help when its wearer has a seizure. The field it came from had begun twelve years earlier with a technical report that colleagues warned Picard could end her career, because serious engineers did not work on emotion.*

## Definition

### Formal

**Affective computing** is "computing that relates to, arises from, or deliberately influences emotion" (Picard, 1995). It has three parts: **recognising** a person's affective state from signals such as facial movement, voice, words, posture, heart rate and skin conductance; **responding** in a way that takes that state into account; and, sometimes, **expressing** something like emotion, as a social robot or a voice assistant does. Every recognition system performs an **inference**: from a measured signal, to a displayed behaviour, to an inner state that cannot be measured directly.

### Intuitive

A machine never measures a feeling. It measures a face, a voice, a sentence or a palm, and guesses. Almost everything worth knowing about this field is about the distance between the measurement and the guess: how much each signal can actually carry, for whom the guess goes wrong, and who is allowed to act on it.

### 中文锚点

你在手机上给朋友回了一串"哈哈哈哈"，脸上其实一点表情都没有。拍集体照的时候，摄影师喊"一二三，茄子"，所有人都笑了，可没有谁是因为开心才笑的；服务员对你微笑，是因为这是她的工作。反过来，真正高兴的时候，很多人也只是安安静静地坐着。笑是做给别人看的动作，高兴是自己心里的感受，两者经常一起出现，却不是同一件事。机器能看到的只有前一样：摄像头拍到嘴角上扬，麦克风录到声音变高，手环量到手心出汗，然后它再去猜后一样。所以哪怕它认"笑脸"认得百分之百准确，它猜"高兴"也可能只对一半，因为问题不出在摄像头上，而出在"从表情到心情"这一步。明白了这一点，就知道什么时候可以相信这类机器，比如提醒一个快睡着的司机，因为闭眼和打哈欠就是疲劳本身；也知道什么时候不该让它替人做决定，比如靠一张脸来判断一个学生有没有认真听讲。

### 术语对照 (Terms)

情感计算 affective computing · 情绪识别 emotion recognition · 情感分析 sentiment analysis · 效价 valence · 唤醒度 arousal · 面部动作单元 facial action unit · 基本情绪 basic emotions · 表达规则 display rules · 韵律 prosody · 皮肤电活动 electrodermal activity (skin conductance) · 心率变异性 heart-rate variability · 基础比率 base rate · 误报 false positive · 生物识别数据 biometric data · 端侧推理 on-device inference

---

## Part I — A chain of inferences

![[affective-computing-chain.svg|860]]

Between what a person feels and what somebody decides about them there are four steps, and each loses information.

1. **Feeling to display.** People show less than they feel, more than they feel, and things they do not feel. Every culture teaches **display rules** about which feelings may be shown to whom. The same inner state produces different faces in different people, and the same face comes from different states.
2. **Display to recording.** Lighting, camera angle, a beard, a mask, a noisy room, a wristband that slips.
3. **Recording to label.** A model trained on examples that somebody labelled, using somebody's theory of what emotions there are.
4. **Label to decision.** A probability gets read as a fact, and a fact gets acted on.

The engineering is mostly in steps 2 and 3, and it is good. The trouble is mostly in steps 1 and 4.

### What is being recognised?

Two descriptions of emotion compete, and the choice decides what a system outputs.

The **categorical** view, associated with Paul Ekman's work from the late 1960s, holds that there are a few **basic emotions** (happiness, sadness, anger, fear, disgust, surprise), each with its own universal facial expression. A classifier built on it outputs one of six or seven labels.

The **dimensional** view (James Russell's circumplex, 1980) describes a state by two numbers: **valence**, how pleasant or unpleasant, and **arousal**, how activated or quiet. Emotion words become regions of a plane.

![[affective-computing-circumplex.svg|820]]

The plane explains a pattern that runs through everything below. Signals driven by the body's activation (sweat, heart rate, the pitch and loudness of a voice) read the **vertical** axis well and the horizontal one hardly at all. Words read the **horizontal** axis. No single signal reads both, which is why terror and elation, side by side at the top of the plane, are so easily confused by a machine.

![[affective-computing-shadows.mp4]]
*A person's state moves round the plane. The skin sensor reports only its shadow on the vertical axis, the words only its shadow on the horizontal one. When delight turns into fury the skin reading does not move at all.*

---

## Part II — The signals, and what each can carry

Each signal below is tested in `affective-computing-lab.py`. The people in it are synthetic models, labelled as such; the signal processing and the arithmetic are real.

### The voice: how something is said

**Prosody** is everything in speech except the words: pitch, loudness, pace, pauses. Activation raises the pitch, widens its range, and speeds and loudens the speech. The lab synthesises four short hummed "utterances" with typical settings, recovers the pitch from the audio by autocorrelation (the period at which the waveform best matches a shifted copy of itself, as in [[Sound]]), and classifies a few hundred noisy variations.

calm: ![[affective-voice-calm.wav]]

sad: ![[affective-voice-sad.wav]]

angry: ![[affective-voice-angry.wav]]

joyful: ![[affective-voice-joyful.wav]]

![[affective-computing-voice-confusion.svg|760]]

Listen to the last two. Measured pitch is 178 Hz against 187 Hz, loudness and pace nearly the same. The classifier separates *excited* from *quiet* **100 %** of the time and cannot tell rage from delight: of 18 angry utterances it calls 8 joyful. A call-centre system that flags "agitated customers" from prosody is measuring something real. One that claims to hear *anger* is reading the wrong axis.

### The words: what is said

**Sentiment analysis** estimates valence from text. The simplest version adds up a score for each word from a list.

```python
LEXICON = {"love": 2, "great": 2, "perfect": 2, "hate": -2, "awful": -2, "boring": -1}   # and so on
NEGATORS = {"not", "never", "no", "nothing", "hardly", "can't", "didn't"}

def score(text, handle_negation=False):
    total, flip = 0, 0
    for w in (w.strip(",.!?").lower() for w in text.split()):
        if handle_negation and w in NEGATORS:
            flip = 4                       # reverse sentiment words in the next few positions
            continue
        v = LEXICON.get(w, 0)
        total += -v if flip and v else v
        flip = max(0, flip - 1)
    return total
```

| Forty test sentences | word list only | with the negation rule |
|---|---|---|
| plain ("The food was wonderful") | 20 of 20 | 20 of 20 |
| negation ("It was never boring") | 0 of 10 | 9 of 10 |
| sarcasm ("Oh great, another Monday test") | 0 of 10 | 0 of 10 |

A rule repairs negation. Nothing inside the sentence repairs sarcasm, because its meaning depends on knowing what Mondays and tests are like. Modern language models do far better than a word list, for the reason that they carry that background, and they still fail on irony within a community they have not seen. Note also what text measures: what someone chose to write, which is step 1 of the chain again.

### The skin and the heart

The palms sweat slightly with any activation of the sympathetic nervous system. Two electrodes measure the resulting change in **skin conductance**: a slow drift, plus a sharp rise one to two seconds after anything arousing, decaying over several seconds. The lab builds such a signal and finds the responses from the slope alone.

![[affective-computing-skin.svg|820]]

All four events are found, to within 1.4 s. Two were dread and two were delight, and **the four responses have the same shape**. The palm reports how much, never which. The same is true of heart rate. This is also why the seizure wristband is sound engineering and a "wristband that knows you are anxious about the exam" is not: the first detects a bodily event, the second guesses at its meaning.

### The face

The careful way to describe a face is the **Facial Action Coding System** (Ekman and Friesen, 1978): some forty **action units**, each one visible muscle movement, such as AU12 (lip corners pulled up) or AU4 (brow lowered). Detecting action units from video is a well-posed vision problem and modern networks do it well. The contested step is the next one, from "AU6 + AU12" to "this person is happy".

In 2019 five senior researchers, chosen because they disagreed with one another, reviewed over a thousand studies for the Association for Psychological Science (Barrett, Adolphs, Marsella, Martinez and Pollak). Their shared conclusion: people do sometimes smile when happy and scowl when angry, more often than chance, but **not reliably and not specifically enough to infer the emotion from the face**. The same expression accompanies different states; the same state comes with different expressions; both vary with culture, situation and individual. A scowl may be anger, concentration, or a bad smell.

---

## Part III — Why an accurate detector gives an inaccurate answer

![[affective-computing-smiles.mp4]]
*A hundred people, thirty of them happy. Forty-two are smiling. A detector that never misses a smile flags all forty-two, and half of them are not happy.*

This is [[Conditional Probability]], and it is the most important calculation in the field. Suppose 30 % of people in a room are happy, people smile 70 % of the time when happy and 30 % of the time when not (politeness, nerves, a camera), and the detector finds smiles with 99 % accuracy.

![[affective-computing-smiles.svg|860]]

$$P(\text{happy} \mid \text{flagged}) = \frac{0.30 \times 0.70}{0.30 \times 0.70 + 0.70 \times 0.30} = 50\,\%.$$

Used as a happiness detector it is right 70 % of the time overall, exactly what you would score by answering "not happy" for everyone. The rates are illustrative, and the structure of the result does not depend on them: **the accuracy printed on the box belongs to step 3 of the chain, and the claim being sold belongs to step 1.** No improvement to the camera or the network touches it.

### Who gets misread

Train a classifier on one group's faces and apply it to a group whose *resting* face differs slightly, here a brow that sits a little lower.

![[affective-computing-misread.svg|820]]

| | accuracy | calm faces labelled angry |
|---|---|---|
| group A (the training data) | 94.5 % | 2.0 % |
| group B | 86.4 % | 16.5 % |

The same software calls a calm face angry **eight times as often** in group B. Nothing about B's feelings differs. This is the mechanism behind a 2018 finding by Lauren Rhue, who ran portraits of professional basketball players through two commercial services: both scored Black players as angrier or more contemptuous than white players with comparable smiles. Similar gaps appear for age, for faces with paralysis or scarring, and for autistic people, whose expressions often do not follow the majority pattern. Collecting more data from group B helps only if the labels for B are right, and labels are made by people looking at faces, which is the step in question.

### Rare events

A system sold to flag employees "about to become violent" is 95 % accurate both ways. In a workforce of 10 000 where ten people really are, it flags 509: 9.5 rightly and 500 wrongly. **A flag is right 1.9 % of the time.** Any screening for something rare produces mostly false alarms; [[Conditional Probability]] works the general case. When the alarm costs the flagged person a job interview or a visit from security, the arithmetic is the ethics.

---

## Part IV — Why this can only be deployed on top of privacy engineering

A face, a voice and a heartbeat are **biometric data**, and an inferred mood is about as personal as information gets. Under both GDPR and PIPL such data is in the specially protected category ([[Data Protection and Privacy]]), and under either law the question "who receives the raw signal?" decides whether a product is possible at all. The architecture that answers it comes from [[Privacy-Preserving Computation]]:

- **Infer on the device.** One minute of face video is about 19 MB; one minute of derived valence and arousal, at one pair per second, is 480 bytes: forty thousand times less, and with no face in it. If the model runs on the phone or in the car, the face never exists anywhere else.
- **Improve the model by federated learning with secure aggregation**, so that no server sees any individual's update, and add **differential privacy** so that the aggregate does not betray anyone either.
- **Prove it.** An attested enclave or an open-source on-device model lets an outsider check that the raw signal stays put. Users have no reason to take a vendor's word for it.

This is the sense in which the two subjects belong together: nobody agrees to be read by a system that ships their face to a server. And it is only half the matter. **Privacy engineering controls where the data goes. It does nothing about whether the inference is true** or whether anyone should be acting on it. A system can be perfectly private and perfectly wrong.

### The law, as it stands

In the European Union, the AI Act defines an *emotion recognition system* as one "for the purpose of identifying or inferring emotions or intentions of natural persons on the basis of their biometric data". Since **2 February 2025** it has been **prohibited to use such systems in workplaces and educational institutions**, except for medical or safety reasons, with fines of up to €35 million or 7 % of worldwide turnover. The Commission's guidelines read the exceptions narrowly: monitoring staff for stress or burnout is not "medical", while detecting fatigue in a pilot is allowed. Indeed physical states such as **pain and fatigue are not "emotions" under the Act at all**, and inferring sentiment from *written text* is outside the ban, since text is not biometric. Elsewhere (a shop reading its customers, a car reading its driver's mood) emotion recognition is classed as high-risk and people must be told it is operating. The legislators gave two reasons, and they are the two halves of Part III: the "limited reliability" and "lack of specificity" of the inference, and the imbalance of power between the watcher and the watched. In China, facial information is sensitive personal information under PIPL, needing a specific purpose, sufficient necessity and separate consent, and dedicated rules for face recognition took effect on 1 June 2025. Laws in this area change quickly; check the current text before relying on any summary.

---

## Where it is the working tool

**Driver monitoring.** New car models sold in the EU must carry a drowsiness and attention warning. A camera watches eyelid closure, gaze and yawning. This is the field at its most defensible: the target is a *physical* state that the signal measures nearly directly, the response is a beep and not a judgement, the computation stays in the car, and being wrong costs little.

**Medicine.** The seizure wristband of the opening story. Tools that help autistic children practise reading faces, and help their teachers notice rising distress before a meltdown, which was the original purpose of Picard's wristbands. Monitoring of depression from changes in a patient's own voice and activity over weeks, where the comparison is with the same person and not with a population.

**Testing and design.** Advertisers show a film to paid, consenting volunteers and record where faces move, which was the business of Affectiva, the company Picard co-founded in 2009. Game studios measure arousal to find where a level drags. In both the claim is modest: something happened here, to many people at once.

**Where it went wrong.** A recruitment platform scored candidates' facial movements in video interviews until 2021, when it withdrew the feature under criticism that the scores had no demonstrated link to job performance. In 2018 a secondary school in Hangzhou installed cameras that classified each student's expression every thirty seconds and scored attentiveness; it was suspended soon afterwards, following a public outcry. In 2022 Microsoft retired the emotion-recognition feature of its face service, citing the lack of scientific agreement on what it measured. Each of these failed at step 1 or step 4 of the chain, and none at the camera.

**Machines that respond.** A voice assistant that slows down when you sound flustered, a tutoring program that offers a hint when your typing falters, a companion chatbot that mirrors your mood. Here the question reverses: the system is now *influencing* emotion, the third clause of Picard's definition, and a product tuned to keep you talking is tuned to be needed. The reward-loop argument of [[You Are a Reinforcement Learner]] applies with full force.

---

## Hands-on

Run `python3 affective-computing-lab.py` (numpy and the standard library, a few seconds); it writes the four voices beside itself.

1. **Make rage and delight separable, or fail to.** In `PROSODY`, change only the settings for "joyful" until the classifier stops confusing it with "angry". What did you have to change, and would a real joyful voice oblige?
2. **Break the word list.** Write five sentences that score positive and mean the opposite. Then try to write a rule that fixes them without breaking the twenty plain sentences.
3. **Move the base rate.** In `smile_is_not_joy()`, set `p_happy` to 0.8 (a wedding) and to 0.05 (a dentist's waiting room). When is a smile good evidence?
4. **Read your own signals.** For one day, note each time you smiled and what you actually felt. Count how many were joy.

---

## Worked examples — every tool named

### Example 1 — the flag that is wrong 98 % of the time

*A school buys a system advertised as "96 % accurate at detecting students who are distressed". In a school of 1500, suppose 30 students are distressed on a given day, and the 96 % applies both to catching them and to clearing the rest. How many students are flagged, and what fraction of flags are right?*

*Trigger: a rare condition and an accuracy quoted without a base rate. Tool: count true and false positives separately.* True positives: $0.96 \times 30 = 28.8$. False positives: $0.04 \times 1470 = 58.8$. Flagged: about 88, of whom 29 are distressed: **33 %**. Two flags in three point at a student who is fine. And the 96 % itself was measured against labels that people assigned by looking at faces, so even the 29 are "distressed according to the labelling scheme".

### Example 2 — which axis?

*For each signal say whether it mainly carries arousal, valence or neither, and give the reason: (a) heart rate; (b) the words of a product review; (c) the loudness of a voice; (d) pupil diameter; (e) typing speed.*

*Tool: the circumplex of Part I; ask what bodily or linguistic mechanism produces the signal.* (a) Arousal: the sympathetic nervous system speeds the heart for fear and for joy alike (and for climbing stairs). (b) Valence: words name evaluations. (c) Arousal. (d) Arousal, and also light level and mental effort, which must be controlled for. (e) Neither reliably: it changes with arousal, fatigue, the keyboard and the task. *The trap:* a signal that moves when emotion changes is not thereby a measure of emotion; it must move for nothing else.

### Example 3 — lawful or not?

*Under the EU AI Act as applicable since February 2025, classify each use. (a) A call centre analyses agents' voices to score their "empathy" for performance reviews. (b) A lorry's camera sounds an alarm when the driver's eyes close. (c) A university proctoring tool flags "nervous" faces during online exams. (d) A supermarket's cameras estimate customers' reactions to a display. (e) A company analyses the sentiment of staff survey comments.*

*Tool: three questions in order. Is it inferring emotion from biometric data? Is it in a workplace or an educational institution? Is it for medical or safety reasons?* (a) **Prohibited**: emotion, from voice, of workers, for evaluation. (b) **Allowed**: fatigue is a physical state, and the purpose is safety. (c) **Prohibited**: emotion from faces in education. (d) Not prohibited, since customers are not employees, but **high-risk**, with a duty to inform. (e) **Outside the ban**: written text is not biometric data, though data-protection law still applies.

### Example 4 — what should leave the phone?

*A meditation app wants to show users a weekly chart of how stressed they were, using the phone's camera to estimate heart rate from tiny colour changes in the face, and wants to improve its model across users. Design the data flow.*

*Tool: Part IV, in order of strength.* Estimate the heart rate and the stress score **on the device**; store the daily numbers on the device; draw the chart there. Nothing need be uploaded for the feature to work. To improve the model, use **federated learning with secure aggregation**, plus differential-privacy noise on the aggregate, so that the server holds a model and no person's data. Publish the on-device model so that the claim can be checked. What this does not settle: whether "stress" is a fair name for a fast pulse, which should be stated to the user as "heart rate was elevated", the thing actually measured.

### Example 5 — read a confusion matrix

*From the voice experiment: of 18 angry utterances, 10 were labelled angry and 8 joyful; of 16 joyful ones, 13 joyful and 3 angry. Calm and sad were never confused with either. Find (a) the precision of the label "angry", (b) the recall for angry speech, (c) the accuracy of "excited or not".*

*Tool: precision is "of those labelled X, how many were X"; recall is "of those that were X, how many were labelled X".* (a) Labelled angry: $10 + 3 = 13$, of which 10 were: **77 %**. (b) $10/18 =$ **56 %**. (c) No excited utterance was ever labelled calm or sad, nor the reverse: **100 %**. The same classifier is excellent or mediocre depending on which question it is asked.

### Example 6 — a design review

*A company proposes cameras in its warehouse that detect "frustration" so that managers can "offer support". Give three objections that would survive even if the camera were perfect.*

(1) **Inference**: a frustrated-looking face is not reliably a frustrated person, and resting faces differ between people and groups, so the errors will not fall evenly. (2) **Power**: the watched cannot refuse, cannot see the scores and cannot contest them, and will learn to perform calm, which destroys the signal and adds a new burden. (3) **Purpose**: the same data serves discipline as easily as support, and nothing technical prevents the change of use. In the EU the proposal is simply unlawful; the three objections are why.

---

## Common Misconceptions (Teaching Notes)

### 1. "A facial expression shows what the person feels"
It shows what the face is doing. Expressions are partly signals to others, governed by culture and situation, and the mapping to inner states is loose in both directions.

### 2. "The system is 95 % accurate, so its conclusions are 95 % reliable"
The accuracy describes one link of the chain, usually detecting the display. The reliability of the conclusion depends on the link before it and on the base rate.

### 3. "Bias can be fixed by adding more diverse data"
More data helps only if its labels are right, and the labels come from people judging faces. If the underlying mapping differs between groups, a single model cannot fit both.

### 4. "If it runs on the device, it is harmless"
On-device inference solves where the data goes. It does nothing about whether the inference is valid or what is done with the result.

### 5. "Emotion recognition is banned in Europe"
It is banned in workplaces and education, from biometric data, with medical and safety exceptions. Elsewhere it is regulated as high-risk. Fatigue and pain detection, and sentiment analysis of text, are outside the ban.

### 6. "Machines that express emotion have emotions"
A robot that smiles is running an output routine chosen for its effect on you. Whether anything is felt is the question of [[The Turing Test]], and nothing in this field answers it.

---

## Exam Notes

**No school syllabus examines affective computing by name.** A search of Cambridge 9618 (2027–29) and 0478 (2026–28), the IB Computer Science guide (first assessment 2027) and the AP Computer Science A course description finds no mention of emotion recognition, affective computing or sentiment analysis.

**What it illustrates that is examined.** IB Computer Science **A4.4** (ethical considerations of machine learning) lists accountability, fairness, bias, consent, privacy and societal impact; this topic supplies a concrete case for each, and Parts III and IV are written to be usable as one. Cambridge 9618 **§7.1** (ethics, including the impact of AI) and **§18.1** (artificial intelligence) and 0478 **§6.3** accept applications of AI and their social consequences as examples; the examinable content itself is in [[Artificial Intelligence]] and [[Ethics and Ownership]]. The probability in Part III is ordinary conditional probability, examined on every mathematics board that includes it ([[Conditional Probability]]).

---

## Connections

- **Builds on:** [[Artificial Intelligence]] — classifiers, training data and how a model learns a boundary; [[Conditional Probability]] — base rates and why a positive result can be mostly wrong; [[Data Protection and Privacy]] — biometric data as a protected category, consent and power; [[Privacy-Preserving Computation]] — on-device inference, federated learning and attestation, without which none of this is deployable.
- **Ethics:** [[Ethics and Ownership]] — the builder as the only early checkpoint, and proxies that smuggle bias back in; [[You Are a Reinforcement Learner]] — what a system optimised for your engagement does to you.
- **Signals:** [[Sound]] and [[Sound Encoding]] — pitch, loudness and sampling; [[Sensors and Control Systems]] — what a transducer measures; [[Automated Systems and Robotics]] — sensing, deciding and acting as a loop.
- **The deeper question:** [[The Turing Test]] — behaving as if, against being.

---

## Beyond Syllabus

### Why the basic-emotions idea was so persuasive
Recall that the categorical view assigns each emotion its own face. In the late 1960s Ekman and Friesen showed photographs of posed expressions to the Fore people of Papua New Guinea, who had seen almost no outsiders, and found that they matched faces to stories ("his child has died") far above chance. It seemed to settle the matter. Later critics pointed out what the method assumed: posed faces, a forced choice from a short list, and stories supplied by the experimenter. When people from remote cultures are asked to sort faces freely, the six Western categories do not reliably appear. Both results are real; the dispute is over what they show.

### Constructed emotion
Lisa Feldman Barrett's alternative: the brain does not detect emotions, it **predicts** what bodily sensations mean, using concepts learned from its culture. A racing heart becomes "fear" before an exam and "excitement" before a match. If so, there is no fingerprint of anger in the face or the body to be found, however good the sensor, because anger is a category the perceiver applies and not a state the body broadcasts. Whether or not the theory is right in full, it explains why thirty years of looking for the fingerprints has not produced them.

### Large language models
A language model reads sarcasm far better than a word list, because it has absorbed how people write about Mondays. It will also produce warm, apparently empathetic replies. Both abilities come from text, so both inherit the limits of text: they concern what people say about feelings. A model that says "I understand how hard this is" has predicted a suitable sentence.

---

## Sources

- R. W. Picard, *Affective Computing*, MIT Media Laboratory Technical Report 321 (1995); book, MIT Press (1997). Her account of the seizure recording: "An AI smartwatch that detects seizures", TED (2018).
- L. F. Barrett, R. Adolphs, S. Marsella, A. M. Martinez, S. D. Pollak, *Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements*, Psychological Science in the Public Interest 20 (2019).
- J. A. Russell, *A Circumplex Model of Affect*, Journal of Personality and Social Psychology (1980). P. Ekman and W. Friesen, *Facial Action Coding System* (1978).
- L. Rhue, *Racial Influence on Automated Perceptions of Emotions* (2018).
- Regulation (EU) 2024/1689 (the AI Act), Article 3(39), Article 5(1)(f), Recital 18; European Commission, *Guidelines on prohibited artificial intelligence practices* (2025).

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $P(H \mid F) = \dfrac{P(F \mid H)\,P(H)}{P(F)}$ | `P(H \mid F) = \dfrac{P(F \mid H)\,P(H)}{P(F)}` | Bayes: from "flagged" back to "happy" |
| precision $= \dfrac{TP}{TP + FP}$ | `\dfrac{TP}{TP + FP}` | of those flagged, how many are right |
| recall $= \dfrac{TP}{TP + FN}$ | `\dfrac{TP}{TP + FN}` | of the real cases, how many are found |
| (valence, arousal) | `(v, a)` | a point on the circumplex |
