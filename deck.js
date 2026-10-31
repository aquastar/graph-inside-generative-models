const PAPERS=[
{
"r": 1,
"f": "core",
"y": 2009,
"l": "Bullmore 2009",
"t": "Complex brain networks: graph theoretical analysis of structural and functional systems",
"v": "Nature Reviews Neuroscience",
"o": "Brain regions as nodes and correlated activity as edges yield hubs, modules and small worlds",
"tl": "Brains can be read as graphs: regions are nodes, correlated activity is edges.",
"c": "Established the connectome vocabulary of hubs, modules and small worlds that this talk reuses.",
"fam": "Graph view of a model"
},
{
"r": 2,
"f": "core",
"y": 2020,
"l": "You 2020",
"t": "Graph Structure of Neural Networks",
"v": "ICML 2020",
"o": "Clustering coefficient and path length of an architecture's relational graph predict its accuracy",
"tl": "The shape of a network architecture predicts how well it learns.",
"c": "Showed clustering coefficient and path length of the relational graph predict accuracy across MLPs, CNNs and ResNets.",
"fam": "Graph view of a model"
},
{
"r": 3,
"f": "core",
"y": 2021,
"l": "Elhage 2021",
"t": "A Mathematical Framework for Transformer Circuits",
"v": "Transformer Circuits Thread",
"o": "Transformer as a residual stream that heads and MLPs read and write, giving the block-graph vocabulary",
"tl": "A transformer is a shared bus that heads and MLPs read from and write to.",
"c": "Gave the residual-stream picture and split heads into \"where to look\" and \"what to move\".",
"fam": "Graph view of a model"
},
{
"r": 4,
"f": "core",
"y": 2025,
"l": "Joshi 2025",
"t": "Transformers are Graph Neural Networks",
"v": "arXiv",
"o": "Self-attention is message passing on a fully connected token graph",
"tl": "Self-attention is message passing on a fully connected token graph.",
"c": "Framed transformers as graph neural networks that won the hardware lottery.",
"fam": "Graph view of a model"
},
{
"r": 5,
"f": "core",
"y": 2021,
"l": "Horta 2021",
"t": "Extracting knowledge from Deep Neural Networks through graph analysis",
"v": "Future Generation Computer Systems",
"o": "Co-activation graph over neurons analyzed with centrality and community detection",
"tl": "Neurons that fire together can be wired into a graph and analyzed like a brain.",
"c": "Built co-activation graphs of trained networks and ran centrality and community detection on them.",
"fam": "Graph view of a model"
},
{
"r": 6,
"f": "core",
"y": 2024,
"l": "Kofinas 2024",
"t": "Graph Neural Networks for Learning Equivariant Representations of Neural Networks",
"v": "ICLR 2024 (oral)",
"o": "A trained network becomes a graph that a GNN processes with permutation invariance built in",
"tl": "Feed an entire trained network to a graph neural network.",
"c": "Turned weights into a computational graph with built-in permutation invariance for learning over networks.",
"fam": "Graph view of a model"
},
{
"r": 7,
"f": "tools",
"y": 2008,
"l": "Kriegeskorte 2008",
"t": "Representational similarity analysis -- connecting the branches of systems neuroscience",
"v": "Frontiers in Systems Neuroscience",
"o": "Compare systems by their matrices of pairwise response distances instead of matching units",
"tl": "Compare two systems by their tables of pairwise distances, not by matching units.",
"c": "Introduced representational similarity analysis, the root of all later similarity measures.",
"fam": "Tools to compare"
},
{
"r": 8,
"f": "tools",
"y": 2016,
"l": "Li 2016",
"t": "Convergent Learning: Do different neural networks learn the same representations?",
"v": "ICLR 2016",
"o": "Networks from different seeds share subspaces but not basis vectors, found by matching neurons",
"tl": "Networks trained from different seeds share subspaces, not specific neurons.",
"c": "Aligned neurons across seeds and found reliably learned versus idiosyncratic features.",
"fam": "Tools to compare"
},
{
"r": 9,
"f": "tools",
"y": 2019,
"l": "Kornblith 2019",
"t": "Similarity of Neural Network Representations Revisited",
"v": "ICML 2019",
"o": "CKA as the default representation-similarity metric, and why CCA fails for wide layers",
"tl": "CKA became the default score for how alike two representations are.",
"c": "Showed older invariant measures fail for wide layers and that CKA recovers matching layers across seeds.",
"fam": "Tools to compare"
},
{
"r": 10,
"f": "tools",
"y": 2023,
"l": "Davari 2023",
"t": "Reliability of CKA as a Similarity Measure in Deep Learning",
"v": "ICLR 2023",
"o": "CKA can be pushed up or down without changing the computed function",
"tl": "CKA can be pushed up or down without changing what the network computes.",
"c": "Showed a similarity score is a claim that needs a functional check.",
"fam": "Tools to compare"
},
{
"r": 11,
"f": "tools",
"y": 2024,
"l": "Huh 2024",
"t": "The Platonic Representation Hypothesis",
"v": "ICML 2024",
"o": "Representations of large models converge toward a shared model of the world",
"tl": "Bigger models seem to converge toward one representation of the world.",
"c": "The Platonic representation hypothesis, with alignment rising with language-model strength.",
"fam": "Tools to compare"
},
{
"r": 12,
"f": "tools",
"y": 2026,
"l": "Gröger 2026",
"t": "Revisiting the Platonic Representation Hypothesis: An Aristotelian View",
"v": "ICML 2026",
"o": "After null calibration global convergence fades while local neighborhood structure survives",
"tl": "Most of that convergence was size, only local structure survives a null model.",
"c": "Introduced permutation-null calibration for representation similarity and revised Huh 2024.",
"fam": "Tools to compare"
},
{
"r": 13,
"f": "stitch",
"y": 2015,
"l": "Lenc 2015",
"t": "Understanding image representations by measuring their equivariance and equivalence",
"v": "CVPR 2015",
"o": "Stitching layers introduced as a test of whether two representations are equivalent",
"tl": "Two image models are equivalent if a small stitching layer connects them.",
"c": "Invented the stitching layer as a test of representational equivalence.",
"fam": "Stitching"
},
{
"r": 14,
"f": "stitch",
"y": 2021,
"l": "Bansal 2021",
"t": "Revisiting Model Stitching to Compare Neural Representations",
"v": "NeurIPS 2021",
"o": "Good networks trained very differently stitch through one layer with no accuracy loss",
"tl": "Very differently trained good networks stitch with almost no penalty.",
"c": "Made stitching a functional similarity measure and showed stronger bottoms improve weaker tops.",
"fam": "Stitching"
},
{
"r": 15,
"f": "stitch",
"y": 2023,
"l": "Moschella 2023",
"t": "Relative representations enable zero-shot latent space communication",
"v": "ICLR 2023 (notable top 5%)",
"o": "Anchor-relative coordinates make encoders and decoders from different models combine zero-shot",
"tl": "Pick the right coordinates and the stitching adapter shrinks to nothing.",
"c": "Relative representations enable zero-shot combination of encoders and decoders from different seeds.",
"fam": "Stitching"
},
{
"r": 16,
"f": "stitch",
"y": 2025,
"l": "Chen 2025",
"t": "Transferring Linear Features Across Language Models With Model Stitching",
"v": "NeurIPS 2025",
"o": "An affine map between residual streams transfers SAE features, probes and steering vectors across LLMs",
"tl": "One affine map carries probes and steering vectors from a small to a large LLM.",
"c": "Transferred SAE features, probes and steering vectors across language models by stitching residual streams.",
"fam": "Stitching"
},
{
"r": 17,
"f": "stitch",
"y": 2025,
"l": "Smith 2025",
"t": "Functional Alignment Can Mislead: Examining Model Stitching",
"v": "ICML 2025",
"o": "Even clustered noise stitches into trained models, so stitching measures compatibility not shared information",
"tl": "Even clustered noise stitches into an ImageNet model at 100% accuracy.",
"c": "Showed stitching accuracy measures compatibility, not shared information.",
"fam": "Stitching"
},
{
"r": 18,
"f": "merge",
"y": 2022,
"l": "Wortsman 2022",
"t": "Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time",
"v": "ICML 2022",
"o": "Fine-tuned models from one checkpoint share a basin, so averaging them beats the best one",
"tl": "Averaging many fine-tunes of one checkpoint beats the best single one.",
"c": "Model soups, explained by fine-tunes sharing one loss basin.",
"fam": "Merging"
},
{
"r": 19,
"f": "merge",
"y": 2023,
"l": "Ainsworth 2023",
"t": "Git Re-Basin: Merging Models modulo Permutation Symmetries",
"v": "ICLR 2023",
"o": "Match hidden units by permutation and independently trained nets become linearly connected",
"tl": "Permute the neurons to match and independently trained nets share a basin.",
"c": "Git Re-Basin, turning neuron alignment into a graph matching step for merging.",
"fam": "Merging"
},
{
"r": 20,
"f": "merge",
"y": 2023,
"l": "Ilharco 2023",
"t": "Editing Models with Task Arithmetic",
"v": "ICLR 2023",
"o": "Weight deltas from fine-tuning are vectors that can be added, negated and combined",
"tl": "A fine-tune is a vector you can add, subtract and combine.",
"c": "Task arithmetic: negate to forget, add to combine, analogies for skills with no data.",
"fam": "Merging"
},
{
"r": 21,
"f": "merge",
"y": 2023,
"l": "Yadav 2023",
"t": "TIES-Merging: Resolving Interference When Merging Models",
"v": "NeurIPS 2023",
"o": "Names the two sources of interference between task vectors and fixes both",
"tl": "Added task vectors interfere through small noise and sign conflicts.",
"c": "TIES-Merging: trim, elect signs, merge only agreeing values.",
"fam": "Merging"
},
{
"r": 22,
"f": "merge",
"y": 2024,
"l": "Hammoud 2024",
"t": "Model Merging and Safety Alignment: One Bad Model Spoils the Bunch",
"v": "Findings of EMNLP 2024",
"o": "Merging imports misalignment from any unsafe expert while capability benchmarks look fine",
"tl": "One unsafe expert makes the whole merge unsafe while capability scores stay fine.",
"c": "Showed merging transfers misalignment as easily as expertise.",
"fam": "Merging"
},
{
"r": 23,
"f": "prune",
"y": 2019,
"l": "Frankle 2019",
"t": "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks",
"v": "ICLR 2019",
"o": "Sparse subnetworks train to full accuracy, so most of a network is removable",
"tl": "A sparse 10 to 20% of the weights trains to full accuracy from the original init.",
"c": "The lottery ticket hypothesis: which weights you keep matters.",
"fam": "Pruning and layer surgery"
},
{
"r": 24,
"f": "prune",
"y": 2019,
"l": "Voita 2019",
"t": "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned",
"v": "ACL 2019",
"o": "Few heads matter, they have readable roles, and they survive pruning last",
"tl": "Only a few attention heads matter and they have readable jobs.",
"c": "Pruned heads with L0 gates, the specialized heads survive last.",
"fam": "Pruning and layer surgery"
},
{
"r": 25,
"f": "prune",
"y": 2025,
"l": "Gromov 2025",
"t": "The Unreasonable Ineffectiveness of the Deeper Layers",
"v": "ICLR 2025",
"o": "Delete the most self-similar block of layers and heal, performance holds until about half the depth is gone",
"tl": "Delete the most self-similar block of layers and QA scores hold until about half are gone.",
"c": "Layer pruning by input-output similarity plus light healing.",
"fam": "Pruning and layer surgery"
},
{
"r": 26,
"f": "prune",
"y": 2025,
"l": "Sun 2025",
"t": "Transformer Layers as Painters",
"v": "AAAI 2025",
"o": "Middle layers share a representation space and tolerate skipping and shuffling, first and last do not",
"tl": "Middle layers share a workspace and tolerate skipping and shuffling.",
"c": "Layers as painters: first and last are indispensable, the middle is permutation tolerant.",
"fam": "Pruning and layer surgery"
},
{
"r": 27,
"f": "prune",
"y": 2026,
"l": "Shrestha 2026",
"t": "On the Limits of Layer Pruning for Generative Reasoning in Large Language Models",
"v": "arXiv",
"o": "Pruning that keeps classification scores destroys generative reasoning that recovery does not restore",
"tl": "Pruning that keeps classification scores destroys generative reasoning.",
"c": "Showed recovery fine-tuning restores classification but not GSM8K or HumanEval.",
"fam": "Pruning and layer surgery"
},
{
"r": 28,
"f": "steer",
"y": 2023,
"l": "Zou 2023",
"t": "Representation Engineering: A Top-Down Approach to AI Transparency",
"v": "arXiv",
"o": "Population-level activation representations as the unit of reading and controlling concepts",
"tl": "Read and control concepts like honesty from populations of activations.",
"c": "Representation engineering as a top-down framing for steering.",
"fam": "Steering"
},
{
"r": 29,
"f": "steer",
"y": 2024,
"l": "Rimsky 2024",
"t": "Steering Llama 2 via Contrastive Activation Addition",
"v": "ACL 2024",
"o": "Mean difference of paired activations, added at generation, turns a behavior up or down",
"tl": "Add the mean activation difference and a behavior turns up or down.",
"c": "Contrastive activation addition: one vector, no training, six behaviors steered.",
"fam": "Steering"
},
{
"r": 30,
"f": "steer",
"y": 2024,
"l": "Arditi 2024",
"t": "Refusal in Language Models Is Mediated by a Single Direction",
"v": "NeurIPS 2024",
"o": "One residual direction controls refusal and can be removed as an activation or a weight edit",
"tl": "One residual direction mediates refusal in 13 chat models.",
"c": "Erasing or adding the direction controls refusal, and it can be baked into the weights.",
"fam": "Steering"
},
{
"r": 31,
"f": "steer",
"y": 2024,
"l": "Tan 2024",
"t": "Analyzing the Generalization and Reliability of Steering Vectors",
"v": "NeurIPS 2024",
"o": "Steerability varies per input, rides on spurious features and breaks out of distribution",
"tl": "Steering works on average but not per input, and sometimes backwards.",
"c": "Measured per-input steerability and its dependence on spurious features.",
"fam": "Steering"
},
{
"r": 32,
"f": "steer",
"y": 2026,
"l": "Xu 2026",
"t": "Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics",
"v": "ACL 2026",
"o": "Weight editing, LoRA and steering are one control-signal update with one preference-utility trade-off",
"tl": "Weight editing, LoRA and steering are one update at three persistence levels.",
"c": "A unified control-signal view with a shared preference-versus-coherence trade-off.",
"fam": "Steering"
},
{
"r": 33,
"f": "ft",
"y": 2024,
"l": "Prakash 2024",
"t": "Fine-Tuning Enhances Existing Mechanisms: A Case Study on Entity Tracking",
"v": "ICLR 2024",
"o": "The same circuit exists before and after fine-tuning, the update strengthens it",
"tl": "Fine-tuning strengthens the existing circuit rather than building a new one.",
"c": "Path patching shows the same entity-tracking circuit before and after math and code fine-tuning.",
"fam": "Fine-tuning"
},
{
"r": 34,
"f": "ft",
"y": 2024,
"l": "Lee 2024",
"t": "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity",
"v": "ICML 2024 (oral)",
"o": "DPO bypasses toxic MLP vectors rather than removing them, so toxicity can be restored",
"tl": "DPO reduces toxicity by routing around the toxic mechanism, which stays intact.",
"c": "Mechanistic account of alignment as bypass, with a simple intervention restoring toxicity.",
"fam": "Fine-tuning"
},
{
"r": 35,
"f": "ft",
"y": 2026,
"l": "Minder 2026",
"t": "Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences",
"v": "ICLR 2026",
"o": "Base-versus-fine-tuned activation deltas reveal the fine-tuning domain even on unrelated text",
"tl": "The activation difference between base and fine-tuned model reveals what the fine-tune was about.",
"c": "Read narrow fine-tuning domains from activation deltas on unrelated text.",
"fam": "Fine-tuning"
},
{
"r": 36,
"f": "unlearn",
"y": 2024,
"l": "Li 2024",
"t": "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning",
"v": "ICML 2024",
"o": "Hazardous-knowledge benchmark and RMU, unlearning by steering internal representations",
"tl": "Steer internal representations on hazardous inputs and the model forgets them.",
"c": "WMDP benchmark and RMU unlearning with general knowledge preserved.",
"fam": "Unlearning"
},
{
"r": 37,
"f": "unlearn",
"y": 2025,
"l": "Hu 2025",
"t": "Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning",
"v": "ICLR 2025",
"o": "A small benign fine-tune brings unlearned knowledge back, so unlearning suppresses rather than forgets",
"tl": "A small harmless fine-tune brings unlearned knowledge back.",
"c": "Showed unlearning methods suppress outputs rather than remove knowledge.",
"fam": "Unlearning"
},
{
"r": 38,
"f": "unlearn",
"y": 2025,
"l": "Guo 2025",
"t": "Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization",
"v": "ICML 2025 (spotlight)",
"o": "Targeting mechanistically located components makes unlearning and edits robust to relearning",
"tl": "Unlearning aimed at the mechanistically located circuit survives relearning.",
"c": "Compared mechanistic versus output-based localization for robust unlearning and editing.",
"fam": "Unlearning"
},
{
"r": 39,
"f": "editing",
"y": 2021,
"l": "Geva 2021",
"t": "Transformer Feed-Forward Layers Are Key-Value Memories",
"v": "EMNLP 2021",
"o": "Feed-forward layers store pattern-to-token memories, the basis of the facts-in-MLPs picture",
"tl": "Feed-forward layers act as key-value memories.",
"c": "Keys match text patterns, values push next-token distributions, the basis of facts in MLPs.",
"fam": "Knowledge editing"
},
{
"r": 40,
"f": "editing",
"y": 2022,
"l": "Meng 2022",
"t": "Locating and Editing Factual Associations in GPT",
"v": "NeurIPS 2022",
"o": "Causal tracing locates facts in mid-layer MLPs and ROME rewrites one with a rank-one update",
"tl": "Facts live in mid-layer MLPs and one can be rewritten with a rank-one update.",
"c": "Causal tracing plus ROME, the locate-then-edit paradigm.",
"fam": "Knowledge editing"
},
{
"r": 41,
"f": "editing",
"y": 2023,
"l": "Hase 2023",
"t": "Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models",
"v": "NeurIPS 2023 (spotlight)",
"o": "Where a fact is located is not where editing works best",
"tl": "Where a fact is stored is not where editing works best.",
"c": "Showed causal-tracing localization does not predict edit success, correlation minus 0.13.",
"fam": "Knowledge editing"
},
{
"r": 42,
"f": "editing",
"y": 2024,
"l": "Cohen 2024",
"t": "Evaluating the Ripple Effects of Knowledge Editing in Language Models",
"v": "TACL",
"o": "One edit implies many others, and editors fail to propagate them",
"tl": "One edit implies many others, and editors fail to propagate them.",
"c": "RippleEdits benchmark for the implied consequences of an edit.",
"fam": "Knowledge editing"
},
{
"r": 43,
"f": "editing",
"y": 2024,
"l": "Yang 2024",
"t": "The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse",
"v": "Findings of ACL 2024",
"o": "A single edit can collapse general ability and perplexity is a cheap warning signal",
"tl": "A few edits can collapse a model, and perplexity warns early.",
"c": "The butterfly effect of editing, with perplexity as a cheap risk signal.",
"fam": "Knowledge editing"
},
{
"r": 44,
"f": "editing",
"y": 2025,
"l": "Yang 2025",
"t": "The Mirage of Model Editing: Revisiting Evaluation in the Wild",
"v": "ACL 2025",
"o": "Editing success falls from 96.8 to 38.5 percent under realistic generation",
"tl": "Editing success falls from 96.8% to 38.5% under realistic evaluation.",
"c": "Showed teacher-forced benchmarks overstate editing success by construction.",
"fam": "Knowledge editing"
},
{
"r": 45,
"f": "editing",
"y": 2025,
"l": "Fang 2025",
"t": "AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models",
"v": "ICLR 2025 (oral, outstanding paper)",
"o": "Project the edit onto the null space of preserved knowledge and preserved outputs stay unchanged",
"tl": "Project the edit onto the null space of preserved knowledge and nothing else moves.",
"c": "AlphaEdit, about 37% improvement for locate-then-edit methods with one line of code.",
"fam": "Knowledge editing"
},
{
"r": 46,
"f": "editing",
"y": 2026,
"l": "Baser 2026",
"t": "CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing",
"v": "Findings of ACL 2026",
"o": "Pre-edit entanglement graph from one layer's activations predicts where ripple effects land",
"tl": "An entanglement graph over facts predicts where an edit will ripple, before the edit.",
"c": "CLaRE, pre-edit ripple prediction from one layer of activations.",
"fam": "Knowledge editing"
},
{
"r": 47,
"f": "diff",
"y": 2013,
"l": "Koutra 2013",
"t": "DeltaCon: A Principled Massive-Graph Similarity Function",
"v": "SDM 2013",
"o": "Principled similarity for two graphs on the same nodes, with attribution of which nodes drove the change",
"tl": "A principled way to compare two graphs on the same nodes.",
"c": "DeltaCon, with attribution of which nodes drove the change in its journal version.",
"fam": "Model diffing"
},
{
"r": 48,
"f": "diff",
"y": 2024,
"l": "Lindsey 2024",
"t": "Sparse Crosscoders for Cross-Layer Features and Model Diffing",
"v": "Transformer Circuits Thread",
"o": "Coins model diffing and gives it a shared dictionary across two models",
"tl": "Compare a model to its earlier self, feature by feature.",
"c": "Named model diffing and introduced sparse crosscoders as its tool.",
"fam": "Model diffing"
},
{
"r": 49,
"f": "diff",
"y": 2025,
"l": "Shuttleworth 2025",
"t": "LoRA vs Full Fine-tuning: An Illusion of Equivalence",
"v": "NeurIPS 2025",
"o": "Equal benchmark scores, different weight-spectrum deltas, different forgetting",
"tl": "LoRA and full fine-tuning reach the same score with different structural deltas.",
"c": "Intruder dimensions in LoRA drive forgetting despite equal benchmarks.",
"fam": "Model diffing"
},
{
"r": 50,
"f": "diff",
"y": 2026,
"l": "Duan 2026",
"t": "Do Activation Monitors Survive Model Updates? Benchmarking, Predicting, and Repairing Activation-Monitor Staleness",
"v": "arXiv",
"o": "Probes break after fine-tuning in predictable ways, so every update needs revalidation",
"tl": "Probes that worked before an update often break after it.",
"c": "Benchmarked, predicted and repaired activation-monitor staleness across updates.",
"fam": "Model diffing"
},
{
"r": 51,
"f": "editing",
"y": 2026,
"l": "Benbrahim 2026",
"t": "Delta-Graph Signatures for Post-Edit Risk Screening in Knowledge Editing",
"v": "SDM 2026",
"o": "Before/after co-activation graph screens which benchmark-perfect edits fail held-out prompts",
"tl": "Knowledge editing family. A before-versus-after block graph ranks which benchmark-perfect edits will fail on unseen prompts.",
"c": "Delta-graph signatures: partial-correlation block graphs before and after an edit, topological and spectral features, AUC 0.703 to 0.797, validated by fact-disjoint transfer and prospective reruns.",
"fam": "Knowledge editing"
}
];
// ---------- Relationship map (Mermaid), highlight per stop ----------
const FAM = {
  tools:  {t:'Tools to compare', sub:['Kriegeskorte 2008: compare distance tables, not coordinates','Kornblith 2019: CKA, the default score','Huh 2024: bigger models look more alike','critique Davari 2023: the score can be gamed','fix Groger 2026: compare to a null model first']},
  core:   {t:'A model is a graph', sub:['Bullmore 2009: brain regions as nodes, co-activity as edges','You 2020: architecture graph statistics predict accuracy','Elhage 2021: blocks as nodes on a shared bus','Horta 2021: the brain recipe applied to a network','Kofinas 2024: feed the whole network to a GNN']},
  stitch: {t:'Stitching', sub:['Bansal 2021: different models stitch for free','critique Smith 2025: even noise stitches']},
  merge:  {t:'Merging', sub:['Wortsman 2022: averaging beats the best','Ilharco 2023: a fine-tune is a vector','critique Hammoud 2024: unsafe comes along']},
  prune:  {t:'Pruning and layer surgery', sub:['Frankle 2019: most weights removable','Gromov 2025: half the layers removable','critique Shrestha 2026: reasoning died quietly']},
  steer:  {t:'Steering', sub:['Rimsky 2024: add one direction, change behavior','Arditi 2024: one direction controls refusal','critique Tan 2024: works on average, not per input']},
  ft:     {t:'Fine-tuning', sub:['Prakash 2024: strengthens the old circuit','Lee 2024: DPO bypasses the toxic mechanism']},
  unlearn:{t:'Unlearning', sub:['Li 2024: steer internal states to forget','critique Hu 2025: benign fine-tune restores it','fix Guo 2025: target mechanistically located parts']},
  editing:{t:'Knowledge editing', sub:['Meng 2022: facts in mid MLPs, rank-one edit','critique Hase 2023: location does not guide editing','critique Yang 2025: success was the test method','fix Fang 2025: null-space projection','Delta-Graph: before/after graph screens risk']},
  diff:   {t:'Model diffing', sub:['Lindsey 2024: the name, a two-model dictionary','Shuttleworth 2025: same score, different delta','Duan 2026: every update breaks old probes','lineage Koutra 2013: compare two graphs on the same nodes']},
};

const STEP={core:0,tools:1,stitch:2,merge:3,prune:4,steer:5,ft:6,unlearn:7,editing:8,diff:9};
const EXPLAIN={
 core:'<b>Start here.</b> Brain regions as nodes and co-activity as edges (Bullmore 2009). A layer as one round of message passing (You 2020). Heads and MLPs as nodes on a shared bus (Elhage 2021). Three ways a model is literally a graph.',
 tools:'<b>Tools to compare.</b> Before comparing a model to its edited self we need a number for how different two networks are. RSA and CKA compare distance tables, not neurons. Davari 2023: the score can be gamed. Groger 2026: compare to a null model first.',
 stitch:'<b>Stitching.</b> If the insides line up, the bottom of one model can drive the top of another through one small connector (Bansal 2021). Smith 2025: even noise stitches. Compatibility is not shared information.',
 merge:'<b>Merging</b>, the weight-space cousin: average instead of connect (Wortsman 2022). A fine-tune is a vector you can add and subtract (Ilharco 2023). Hammoud 2024: the unsafe behavior comes along with the skill.',
 prune:'<b>Pruning.</b> Remove parts and see what breaks. Most weights are removable (Frankle 2019), half the layers too (Gromov 2025). Shrestha 2026: reasoning died while classification scores held. The dashed arrow is an open question: does the editing screen transfer here?',
 steer:'<b>Steering.</b> Nudge the activations at run time along one direction (Rimsky 2024). One direction controls refusal in 13 models (Arditi 2024). Tan 2024: reliable on average, not per input.',
 ft:'<b>Fine-tuning</b>, the most common change and the least inspected. It strengthens the old circuit rather than building a new one (Prakash 2024). DPO bypasses the toxic mechanism instead of removing it (Lee 2024).',
 unlearn:'<b>Unlearning</b> is fine-tuning with a target to forget (Li 2024). Hu 2025: a benign fine-tune brings the knowledge back. Guo 2025: target the mechanistically located parts and the change holds.',
 editing:'<b>Knowledge editing</b>, where the arrows meet. Same object as a task vector and a steering direction. Same phenomenon as unlearning: bypassed, not removed. Meng 2022 founded it, Hase 2023 and Yang 2025 cracked it, Fang 2025 repaired it. Baser 2026 predicts before the edit, Delta-Graph screens after.',
 diff:'<b>Model diffing</b>, the discipline this belongs to: compare a model to its earlier self (Lindsey 2024). Same score, different delta (Shuttleworth 2025). Its lineage is DeltaCon, which compared two graphs on the same nodes in 2013. The talk ends here, with what is still unfilled.'
};
// hand-laid map: 1200 x 620 canvas
const POS = {
  tools:  {x:430,y:8,  w:340}, core:{x:430,y:245,w:340}, diff:{x:430,y:498,w:340},
  stitch: {x:20, y:118,w:340}, merge:{x:20,y:250,w:340}, prune:{x:20,y:392,w:340},
  steer:  {x:840,y:104,w:340}, ft:{x:840,y:214,w:340}, unlearn:{x:840,y:306,w:340}, editing:{x:840,y:428,w:340},
};
const BASER={x:1000,y:560,w:190,h:44};
function nodeH(key,compact){const n=compact?Math.min(2,FAM[key].sub.length):FAM[key].sub.length;return 30+16*n;}
function center(key,compact){const p=POS[key];const h=nodeH(key,compact);return [p.x+p.w/2,p.y+h/2,p.x,p.y,p.w,h];}
function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;');}
let PROG=false; function frag(step,inner){return PROG?`<g class="fragment" data-fragment-index="${step}">${inner}</g>`:inner;}
function edge(x1,y1,x2,y2,cx,cy,label,dashed,arrow,t,step){ t=(t===undefined)?0.5:t;
  const d=(cx===null)?`M${x1},${y1} L${x2},${y2}`:`M${x1},${y1} Q${cx},${cy} ${x2},${y2}`;
  let s=`<path d="${d}" fill="none" stroke="#8a9bab" stroke-width="1.6" ${dashed?'stroke-dasharray="6 5"':''} ${arrow?'marker-end="url(#arr)"':''}/>`;
  if(label){const u=1-t; const mx=cx===null?x1+(x2-x1)*t:u*u*x1+2*u*t*cx+t*t*x2, my=cy===null?y1+(y2-y1)*t:u*u*y1+2*u*t*cy+t*t*y2; const w=label.length*6.6+10;
    s+=`<rect x="${mx-w/2}" y="${my-10}" width="${w}" height="20" rx="4" fill="#fbfbfa" stroke="none"/><text x="${mx}" y="${my+4}" text-anchor="middle" font-size="12" fill="#5b6b7c" font-style="italic">${esc(label)}</text>`;}
  return step===undefined?s:frag(step,s);
}
function mapSvg(here, progressive){
  PROG=!!progressive;
  const compact=false;
  const ORDER2=['tools','stitch','merge','prune','steer','ft','unlearn','editing','diff'];
  const idx=ORDER2.indexOf(here);
  function cls(k){ if(k==='core') return 'core'; if(here==='gaps') return k==='editing'?'here':(['tools','diff'].includes(k)?'':'done'); if(here==='all'||idx<0) return ''; const i=ORDER2.indexOf(k); if(here==='ft'&&k==='unlearn') return 'here'; if(i<idx) return 'done'; if(i===idx) return 'here'; return 'future'; }
  let s='<svg class="map" viewBox="-20 0 1250 620" xmlns="http://www.w3.org/2000/svg"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#8a9bab"/></marker></defs>';
  const C={}; for(const k of Object.keys(POS)) C[k]=center(k,compact);
  const [tx,ty]=C.tools,[cx0,cy0]=C.core,[dx,dy]=C.diff;
  // plain spokes core to families
  for(const k of ['stitch','merge','prune']){const [x,y,nx,ny,w,h]=C[k]; s+=edge(C.core[2],cy0,nx+w,y,null,null,'',false,false,0.5,STEP[k]);}
  for(const k of ['steer','ft','unlearn','editing']){const [x,y,nx,ny,w,h]=C[k]; s+=edge(C.core[2]+C.core[4],cy0,nx,y,null,null,'',false,false,0.5,STEP[k]);}
  s+=edge(tx,C.tools[3]+C.tools[5],cx0,C.core[3],null,null,'metric',false,true,0.5,STEP.tools);
  s+=edge(cx0,C.core[3]+C.core[5],dx,C.diff[3],null,null,'graph comparison',false,true,0.5,STEP.diff);
  s+=edge(C.tools[2],ty+10,C.stitch[2]+C.stitch[4]-40,C.stitch[3],380,40,'inspires',false,true,0.5,STEP.stitch);
  s+=edge(C.stitch[0],C.stitch[3]+C.stitch[5],C.merge[0],C.merge[3],null,null,'cousin',false,true,0.5,STEP.merge);
  s+=edge(C.merge[2]+C.merge[4]-30,C.merge[3]+C.merge[5],C.editing[2],C.editing[1]+10,600,470,'same object',false,true,0.82,STEP.editing);
  s+=edge(C.steer[2]+C.steer[4],C.steer[1],C.editing[2]+C.editing[4],C.editing[1],1250,300,'same object',false,true,0.5,STEP.editing);
  s+=edge(C.ft[0],C.ft[3]+C.ft[5],C.unlearn[0],C.unlearn[3],null,null,'inspires',false,true,0.5,STEP.unlearn);
  s+=edge(C.unlearn[0],C.unlearn[3]+C.unlearn[5],C.editing[0],C.editing[3],null,null,'same phenomenon',false,true,0.5,STEP.editing);
  s+=edge(C.editing[0]-60,C.editing[3]+C.editing[5],C.diff[2]+C.diff[4],dy+20,880,600,'belongs to',false,true,0.5,STEP.diff);
  s+=edge(C.prune[2]+C.prune[4]-40,C.prune[3]+C.prune[5],C.editing[2],C.editing[3]+C.editing[5]-10,600,430,'open',true,true,0.18,STEP.editing);
  s+=edge(BASER.x+BASER.w/2,BASER.y,C.editing[0]+40,C.editing[3]+C.editing[5],null,null,'complement',false,true,0.5,STEP.editing);
  // nodes
  for(const k of Object.keys(POS)){const f=FAM[k];const [x,y,nx,ny,w,h]=C[k];const lines=compact?f.sub.slice(0,2):f.sub;
    s+=`<g class="node ${cls(k)}"><rect x="${nx}" y="${ny}" width="${w}" height="${h}" rx="6"/><text x="${x}" y="${ny+20}" text-anchor="middle">${esc(f.t)}</text>`;
    lines.forEach((l,i)=>{s+=`<text class="sub" x="${x}" y="${ny+36+i*16}" text-anchor="middle">${esc(l)}</text>`;}); s+='</g>'; if(PROG){ s=s.replace(/(<g class="node[^>]*>(?:(?!<\/g>)[\s\S])*<\/g>)$/, m=>frag(STEP[k],m)); } }
  s+=frag(STEP.editing,`<g class="node"><rect x="${BASER.x}" y="${BASER.y}" width="${BASER.w}" height="${BASER.h}" rx="6"/><text x="${BASER.x+BASER.w/2}" y="${BASER.y+18}" text-anchor="middle" style="font-size:14px">Baser 2026</text><text class="sub" x="${BASER.x+BASER.w/2}" y="${BASER.y+34}" text-anchor="middle">predicts ripples before the edit</text></g>`);
  s+='</svg>';
  if(PROG){ s+='<div class="mapexpbox">'; for(const k of Object.keys(STEP)){ const last=k==='diff'; s+=`<div class="mapexp fragment ${last?'':'fade-in-then-out'}" data-fragment-index="${STEP[k]}">${EXPLAIN[k]}</div>`; } s+='</div>'; }
  return s;
}
document.querySelectorAll('section[data-map]').forEach(sec=>{const slot=sec.querySelector('.mapslot'); if(slot) slot.innerHTML=mapSvg(sec.getAttribute('data-map'), sec.hasAttribute('data-progressive'));});
// timeline animation origins from the map layout (fractions of the timeline canvas)
const ORIGIN={}; for(const k of Object.keys(POS)){const [x,y]=center(k,false); ORIGIN[k]=[x/1200,y/620];}

// ---------- Timeline with animation from the map ----------
const FAMCOLOR={core:'#1c2430',tools:'#1f6f8b',stitch:'#1f6f8b',merge:'#2f7d4f',prune:'#8a6d1f',steer:'#6b4e9b',ft:'#3f5f7f',unlearn:'#a3324f',editing:'#b8442c',diff:'#5b6b7c'};
const LANES=[['core','A model is a graph'],['tools','Tools to compare'],['stitch','Stitching'],['merge','Merging'],['prune','Pruning'],['steer','Steering'],['ft','Fine-tuning'],['unlearn','Unlearning'],['editing','Knowledge editing'],['diff','Model diffing']];

// paper-to-paper relations shown on the timeline: [from, to, type]
const REL=[
 ['Bullmore 2009','Horta 2021','inspires'],['Bullmore 2009','Koutra 2013','inspires'],['Kriegeskorte 2008','Kornblith 2019','inspires'],['Li 2016','Kornblith 2019','inspires'],
 ['Kornblith 2019','Davari 2023','critique'],['Kornblith 2019','Huh 2024','inspires'],['Huh 2024','Gröger 2026','fix'],
 ['Lenc 2015','Bansal 2021','inspires'],['Bansal 2021','Moschella 2023','inspires'],['Bansal 2021','Chen 2025','inspires'],['Bansal 2021','Smith 2025','critique'],
 ['Wortsman 2022','Ilharco 2023','inspires'],['Ainsworth 2023','Wortsman 2022','inspires'],['Ilharco 2023','Yadav 2023','fix'],['Ilharco 2023','Hammoud 2024','critique'],
 ['Frankle 2019','Gromov 2025','inspires'],['Voita 2019','Gromov 2025','inspires'],['Gromov 2025','Sun 2025','inspires'],['Gromov 2025','Shrestha 2026','critique'],
 ['Zou 2023','Rimsky 2024','inspires'],['Rimsky 2024','Arditi 2024','inspires'],['Rimsky 2024','Tan 2024','critique'],['Arditi 2024','Xu 2026','inspires'],['Ilharco 2023','Xu 2026','same'],
 ['Prakash 2024','Minder 2026','inspires'],['Lee 2024','Minder 2026','inspires'],['Li 2024','Hu 2025','critique'],['Hu 2025','Guo 2025','fix'],['Lee 2024','Hu 2025','same'],
 ['Geva 2021','Meng 2022','inspires'],['Elhage 2021','Meng 2022','inspires'],['Meng 2022','Hase 2023','critique'],['Meng 2022','Cohen 2024','critique'],['Meng 2022','Yang 2024','critique'],['Yang 2024','Yang 2025','inspires'],['Meng 2022','Fang 2025','fix'],
 ['Koutra 2013','Benbrahim 2026','inspires'],['Horta 2021','Benbrahim 2026','inspires'],['Yang 2024','Benbrahim 2026','inspires'],['Baser 2026','Benbrahim 2026','complement'],['Hase 2023','Benbrahim 2026','inspires'],
 ['Lindsey 2024','Shuttleworth 2025','inspires'],['Shuttleworth 2025','Duan 2026','inspires'],['Benbrahim 2026','Duan 2026','same'],['You 2020','Kofinas 2024','inspires'],['Elhage 2021','Joshi 2025','inspires'],
];
const RELSTYLE={inspires:['#9aa7b0','',1.4],critique:['#c0392b','6 4',1.8],fix:['#2e7d32','',1.6],same:['#6b4e9b','2 4',1.6],complement:['#1f6f8b','8 4',1.4]};
const SEEDINFO=`<b>Benbrahim et al., SDM 2026 (accepted, to appear). Knowledge editing family.</b><br><b>TL;DR:</b> a before-versus-after graph of the edited model ranks which benchmark-perfect edits will fail on unseen prompts.<br><b>Builds on:</b> Koutra 2013 (comparing two graphs on the same nodes), Horta 2021 (co-activation graphs), Yang 2024 (perplexity as a post-edit warning), Hase 2023 (measure post-edit structure, do not assume it). <b>Complements:</b> Baser 2026 (before the edit, we screen after). <b>Same concern:</b> Duan 2026 (every update needs revalidation).<br><b>Contribution:</b> a disjoint behavioral label, partial-correlation block graphs before and after, topological plus spectral summaries, AUC 0.703 to 0.797, validated by fact-disjoint transfer and prospective reruns. Still owed: a null model and attribution.`;
function buildTimeline(){
  const host=document.getElementById('timeline'); if(!host) return;
  const W=1160,H=440,L=148,R=120,T=14,B=30, y0=2008,y1=2026;
  const span=W-L-R, split=2018.5, f=0.13; const x=y=> y<=split ? L+(y-y0)/(split-y0)*span*f : L+span*f+(y-split)/(y1-split)*span*(1-f);
  const laneH=(H-T-B)/LANES.length; const ly=k=>T+LANES.findIndex(l=>l[0]===k)*laneH+laneH/2;
  let s=`<svg id="tlsvg" viewBox="0 0 ${W} ${H}" width="100%" xmlns="http://www.w3.org/2000/svg">`;
  LANES.forEach((l,i)=>{const y=T+i*laneH; s+=`<rect x="0" y="${y}" width="${W}" height="${laneH}" fill="${i%2?'#f4f6f8':'#ffffff'}"/><text x="10" y="${y+laneH/2+4}" font-size="12.5" font-weight="600" fill="${FAMCOLOR[l[0]]}">${l[1]}</text>`;});
  for(let yr=y0;yr<=y1;yr++){  s+=`<line x1="${x(yr)}" y1="${T}" x2="${x(yr)}" y2="${H-B}" stroke="#e3e8ec" stroke-width="1"/><text x="${x(yr)}" y="${H-B+18}" text-anchor="middle" font-size="12" fill="#5b6770">'${String(yr).slice(2)}</text>`;}
  const seen={}; const POSN={}; let dots='';
  // position first, then alternate label rows within each lane by x order so neighbours never share a row
  const placed=PAPERS.map(p=>{const key=p.f+p.y; seen[key]=(seen[key]||0)+1; const k=seen[key]-1; return {p, cx:x(p.y)+k*44, cy:ly(p.f)};});
  LANES.forEach(l=>{ placed.filter(q=>q.p.f===l[0]).sort((a,b)=>a.cx-b.cx).forEach((q,i)=>{ q.row=i%2; }); });
  placed.forEach(({p,cx,cy,row})=>{
    const [ox,oy]=ORIGIN[p.f]; const c=FAMCOLOR[p.f]; POSN[p.l]=[cx,cy];
    const seed=p.l==='Benbrahim 2026'; const ty = row===0 ? -10 : 17;
    dots+=`<g class="dot" data-l="${p.l}" data-x="${cx}" data-y="${cy}" data-ox="${ox*W}" data-oy="${oy*H}" style="transform:translate(${ox*W}px,${oy*H}px)"><circle r="${seed?8:5.5}" fill="${c}" ${seed?'stroke="#1c2430" stroke-width="2"':''}/><text x="${seed?13:0}" y="${seed?4:ty}" font-size="10.5" text-anchor="${seed?'start':'middle'}" fill="#1c2430" ${seed?'font-weight="700"':''}>${p.l}</text></g>`;
  });
  let edges='<g id="tledges">';
  REL.forEach(([a,b,t])=>{ const A=POSN[a],B=POSN[b]; if(!A||!B) return; const [col,dash,w]=RELSTYLE[t]; const mx=(A[0]+B[0])/2, my=(A[1]+B[1])/2-Math.min(40,Math.abs(B[0]-A[0])*0.12+8);
    edges+=`<path class="rel" data-a="${a}" data-b="${b}" data-t="${t}" d="M${A[0]},${A[1]} Q${mx},${my} ${B[0]},${B[1]}" fill="none" stroke="${col}" stroke-width="${w}" ${dash?`stroke-dasharray="${dash}"`:''} opacity="0"/>`; });
  edges+='</g>';
  s+=edges+dots+'</svg>'; host.innerHTML=s;
  const info=document.getElementById('tlinfo'); const DEFAULT=info?info.innerHTML:'';
  const byL={}; PAPERS.forEach(p=>byL[p.l]=p);
  host.querySelectorAll('.dot').forEach(g=>{
    g.addEventListener('mouseenter',()=>{ const l=g.dataset.l;
      host.querySelectorAll('.rel').forEach(e=>{ const on=e.dataset.a===l||e.dataset.b===l; e.classList.toggle('hi',on); e.classList.toggle('dim',!on); });
      host.querySelectorAll('.dot').forEach(o=>o.classList.toggle('dim', o!==g && !REL.some(([a,b])=>(a===l&&b===o.dataset.l)||(b===l&&a===o.dataset.l))));
      if(info){ if(l==='Benbrahim 2026') info.innerHTML=SEEDINFO; else { const p=byL[l]; info.innerHTML=`<b>${p.l}, ${p.v}. ${p.fam}.</b><br><b>TL;DR:</b> ${p.tl}<br><b>Contribution:</b> ${p.c}`; } }
    });
    g.addEventListener('mouseleave',()=>{ host.querySelectorAll('.rel').forEach(e=>e.classList.remove('hi','dim')); host.querySelectorAll('.dot').forEach(o=>o.classList.remove('dim')); if(info) info.innerHTML=DEFAULT; });
  });
}
function animateTimeline(){
  const host=document.getElementById('timeline'); if(!host) return;
  const dots=host.querySelectorAll('.dot');
  dots.forEach(d=>{d.style.transition='none'; d.style.transform=`translate(${d.dataset.ox}px,${d.dataset.oy}px)`; d.style.opacity='0.15';});
  requestAnimationFrame(()=>requestAnimationFrame(()=>{
    dots.forEach((d,i)=>{d.style.transition=`transform 1.4s cubic-bezier(.2,.7,.2,1) ${i*18}ms, opacity .6s ${i*18}ms`; d.style.transform=`translate(${d.dataset.x}px,${d.dataset.y}px)`; d.style.opacity='1';});
    host.querySelectorAll('.rel').forEach(e=>{e.style.transition='opacity .8s 1.9s'; e.setAttribute('opacity','0.55');});
  }));
  host.querySelectorAll('.rel').forEach(e=>{e.style.transition='none'; e.setAttribute('opacity','0');});
}
buildTimeline();
Reveal.on('slidechanged',e=>{ if(e.currentSlide && e.currentSlide.id==='tl-slide') setTimeout(animateTimeline,150); });
Reveal.on('ready',e=>{ if(e.currentSlide && e.currentSlide.id==='tl-slide') setTimeout(animateTimeline,400); });
