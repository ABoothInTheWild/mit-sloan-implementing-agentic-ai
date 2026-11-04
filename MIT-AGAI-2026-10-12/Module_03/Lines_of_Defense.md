# Playbook 3.4: Layer Lines of Defense at Portfolio Scale

**Author:** Alexander Booth
**Date:** November 2026
**Cohort:** MIT-AGAI October 12, 2026

## Overview

The four safeguard layers in Playbook 3.2 (hardcoded constraints, output verification, reversibility by
design, escalation architecture) protect **one agent**. Section 3.4 asks what happens when you have 20 or
50 agents, each set at a different point on the autonomy dial. Olu puts the problem this way in the
Module 3 podcast: the question isn't where the organization sits on the dial, it's how you govern
"20 different positions on that dial arguably at the same time."

You can't hand-build governance for each agent at that scale, so some of it has to become shared
infrastructure that every agent inherits. The playbook splits that infrastructure into three layers. The
foundation layer sets the rules, the operational layer enforces them at runtime, and the transparency
layer documents what's actually running.

## The Three Layers

1. **Foundation layer: data and model governance.** The rules that come before any agent is built: who
   owns which data, what data agents may touch (personal, financial, customer records), which models are
   approved for use, and how model versions are tracked and retired. Most organizations already have
   pieces of this (data classification, privacy policies, vendor risk reviews, model risk management).
   Common gaps: no approved-model list, no rules for an agent combining data across systems, and no owner
   for a vendor model upgrade that quietly changes agent behavior.

2. **Operational layer: runtime guardrails.** Controls that run while agents are working, standardized
   once rather than rebuilt for each agent: input filtering (prompt injection, sensitive data going in),
   output moderation (off-policy or leaked content coming out), routing (which model or agent handles
   which request), and use-case limits (for example, no agent issues a refund over a set amount). The SAP
   "generative AI hub" described in the MIT SMR/BCG reading is a good model: one central hub every
   application goes through, so guardrails, security, and compliance are applied once and inherited
   everywhere. Ownership is usually split: a platform team runs the shared guardrail service, while
   security, legal, and business owners set the policies it enforces. Non-human identity (Playbook 3.5)
   belongs here too, since least-privileged access is itself a portfolio-wide guardrail.

3. **Transparency layer: the AI bill of materials (AI-BOM).** An ingredients list for each agent: its
   models and versions, where training or fine-tuning data came from, prompts and system instructions,
   third-party components and vendors, the tools and APIs it can call, and its change history. It's what
   you need when a vendor changes a model, a regulator asks questions, or something goes wrong and you
   have to trace why. Expect the documentation to be thinnest on vendor training data.

## A Note on "Lines of Defense"

Searching this term will turn up the Institute of Internal Auditors' **Three Lines Model** (formerly
"three lines of defense"). It's related but different. The IIA model splits risk *ownership* (first line:
business teams; second line: risk and compliance; third line: internal audit), while the playbook's three
layers split risk *infrastructure*. A strong 3.4 answer can use both: say who in each line owns each
layer.

## Further Reading

**Foundation layer**
* [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework):
  the most widely used reference for what an AI governance program covers.
  ([PDF](Downloads/NIST%20AI%20Risk%20Management%20Framework%20(AI%20RMF%201.0).pdf))
* [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf): applies
  the AI RMF specifically to generative AI risks.
* [ISO/IEC 42001](https://www.iso.org/standard/42001): the international standard for AI management
  systems, useful if your organization already works with ISO standards.

**Operational layer**
* [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): the most common security
  risks for LLM-based systems and how to mitigate them.
  ([PDF, 2025 edition](Downloads/OWASP%20Top%2010%20for%20LLM%20Applications%202025.pdf))
* [OWASP Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/):
  the same idea, extended to agents that use tools and take actions.

**Transparency layer**
* [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) (Mitchell et al.): the original
  proposal for standardized model documentation.
  ([PDF](Downloads/Model%20Cards%20for%20Model%20Reporting.pdf))
* [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) (Gebru et al.): the companion idea for
  documenting training data.
* [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/): an existing standard format for an AI/ML
  bill of materials.

**Lines of defense**
* [The IIA's Three Lines Model](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/)
  (Institute of Internal Auditors, 2020).

## Writing Your Answer

You don't need to read all of these. The rubric rewards specifics about your own organization: what you
already have, where the gaps are, and who would own each layer. Use the readings to sanity-check your
gaps, not as material to summarize.
