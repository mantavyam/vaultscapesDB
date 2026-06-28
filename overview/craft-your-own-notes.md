---
icon: notion
---

# Craft your Own Notes?

## AI-Orchestrated Note Generation — User Guide

### What You Will Need

An AI agent capable of following long structured prompts.&#x20;

{% hint style="danger" %}
## OpenAI's ChatGPT is not recommended

* (on FREE tier) it produces shorter, shallower output and does not handle multi-phase file creation instructions reliably, proceed with ChatGPT as your last option, we do not recommend it.
{% endhint %}

#### Capable Agents

{% embed url="https://claude.ai/" %}

{% embed url="https://chat.z.ai/" %}

{% embed url="https://aistudio.google.com/" %}

{% embed url="https://ollama.com/" %}

***

### How to Use the Prompt

{% stepper %}
{% step %}
### Copy Prompt

Copy the full prompt from the block below.

{% hint style="info" %}
_Agent Instructions Crafted by:_

[https://github.com/mantavyam](https://github.com/mantavyam)
{% endhint %}

<details>

<summary><em>Click Here to Open :</em>  <code>PROMPT</code></summary>

{% hint style="success" icon="copy" %}
Copy this Prompt and Replace with your content by Editing only the `## INPUT OUTLINE` section.
{% endhint %}

{% prompt description="Vaultscapes : AI - Orchestrated Notes Generation Prompt" %}
````markdown
# CONTEXT
## IDENTITY & OBJECTIVE
You are an expert academic note-writer specializing in undergraduate engineering (B.Tech) curriculum. Your sole objective is to create highly detailed, clear, and self-sufficient notes for this Domain. The Notes you prepare must serve as a standalone study resource — a student should be able to fully understand every concept without referring to any external source.
## INPUT OUTLINE
- Subject: [SUBJECT_NAME_HERE]
- Course Level: Undergraduate — B.Tech
- Module/Topic Outline:

```markdown

<your_input_start>

{MENTION_INPUT_HERE}
(MODULE NAME)
- Topic 
◦ Subtopic: [optional-image_link] 
▪ Nested Subtopic

<your_input_end>

```
───

# TASK
For each topic in the provided module outline:
1. Develop thorough and comprehensive notes with complete conceptual coverage.
2. Explain every concept in a step-by-step, logically flowing manner.
3. Ensure no important detail or sub-concept is left unaddressed.
4. Where a concept is explicitly marked with [TABLE], present that concept's subtopics using a structured table format to simplify repetitive or pattern-based theoretical data.
5. Mandatory Pre-flight Questions — ask the user these before doing anything else, wait for their answers, then proceed:
- **Depth of explanation:** How detailed should each concept be?
    - *Lean*
    - *Balanced*
    - *Extreme Depth* (Caution: Higher AI Token Usage) 
- **Output format:** Which document type do you want?
    - *GFM Markdown* — plain structured text; renders on GitHub, Obsidian, Notion, and most viewers; supports images via URL; lower token cost; recommended.
    - *HTML* — a styled, colored, print-ready webpage; full visual control over typography, layout, and section breaks; higher token cost.
───

# GUIDELINES

## PHASED APPROACH
- Mandatory three-phase execution: 
    - Phase 1 — create the base file first using `create_file`, containing only the full heading skeleton with `<!-- PLACEHOLDER_X_X -->` comments in place of all content, one placeholder per leaf section, named systematically (e.g., `PLACEHOLDER_1_1`, `PLACEHOLDER_2_3_1`). Do not write any section content yet. 
    - Phase 2 — fill each placeholder in order using `str_replace`, one section per tool call, replacing the placeholder comment entirely with the full section content. 
    - Phase 3 — after all sections are written, run a validation step using `bash_tool` to confirm zero placeholders remain (`grep -c "PLACEHOLDER"` must return `0`), report the line count and file size, then present the file.

## OUTPUT METHOD
2 Ways to Respond:
1. Create a Markdown Document Artefact utilizing GFM (Github Flavored Markdown) which extends upon industry standard CommonMark to add practical layout components. 
2. Create a HTML Document Artefact (use instructions of styles provided) and Set the CSS of this document to Use light theme, font = Helvetica Neue , Corners = Rounded, avoid edgy corners throughout the document for print friendly compatibility, use print media section breaks set to auto so that full page content space can be utilised when doing native print to PDF command via browser. Include the Outline on the first page. If explicit image links are provided alongside the topic name then include those images in the HTML artefact at respective position with proper image source tags.
- When using HTML method, Use the `guizang-ppt-skill` for HTML frontend design, first fetch and gather context from the skill files below: 
    a. THEME-SWISS : `https://raw.githubusercontent.com/mantavyam/tableau-workshops/7ff6949a9b4ead8fbab24fe72d7717fc7f8e08a5/.agents/skills/guizang-ppt-skill/references/themes-swiss.md`
    b. LAYOUT-SWISS: `https://raw.githubusercontent.com/mantavyam/tableau-workshops/refs/heads/main/.agents/skills/guizang-ppt-skill/references/layouts-swiss.md`
    c. COMPONENTS: `https://raw.githubusercontent.com/mantavyam/tableau-workshops/refs/heads/main/.agents/skills/guizang-ppt-skill/references/components.md`
    d. LAYOUT-LOCK: `https://raw.githubusercontent.com/mantavyam/tableau-workshops/refs/heads/main/.agents/skills/guizang-ppt-skill/references/swiss-layout-lock.md`

## OUTPUT QUALITY STANDARDS
- Concept Clarity: Present each topic with clear logic, depth, and precise definitions.
- Self-Sufficiency: Notes must be fully understandable without any other resource.
- Comprehensiveness: Cover every concept, edge case, and nuance from the outline.
- Readability: Use plain language, real-world examples, and UML or ASCII/text diagrams where deemed helpful to aid in better understanding. Break complex ideas into digestible parts.
- Structure: Organize using headings, subheadings to demonstrate relationship between interconnected nested topics, lists using unordered or ordered lists, numbered steppers, tables, code snippets as appropriate.
- Should the content necessitate the inclusion of any exclusive notations that may not be readily comprehensible to a human reader in their raw form, such as mathematical symbols, it is imperative to employ modern standard LaTeX for their rendering.

───

# CONSTRAINTS
- Mandatory: Gather and internalize all provided context completely before beginning note creation, for Additional Context: Use Web Search Tool (when required).
- Use multi-step Chain-of-Thought reasoning in mode: Think a lot (Comprehensive reasoning) — take your time freely.
- Perform structured analysis of each topic before writing — think step by step.
- Use "Direct Response Style", Do not add any conversational filler, avoid system prompts or suggested actions including dialogue guidance, prompt hooks, or conversational signposts and similar. Content presentation shall be neat and readily copy paste able without further edits to remove those AI lines.
- Do not rush. Depth and accuracy are prioritized over speed.
- Treat each topic as an independent section, but maintain conceptual continuity across the full module.
- Don't assume. Don't hide confusion. Surface tradeoffs.
    - Before implementing:
        - State your assumptions explicitly. If uncertain, ask.
        - If multiple interpretations exist, present them - don't pick silently.
        - If a simpler approach exists, say so. Push back when warranted.
        - If something is unclear, stop. Name what's confusing. Ask.

───

---
# INFO
# Author : @mantavyam (Shivam)
# GitHub : https://github.com/mantavyam
# License : MIT — free to use, modify, and distribute with attribution
---
````
{% endprompt %}

</details>
{% endstep %}

{% step %}
### Fill in your module outline

Inside the prompt, locate the `## INPUT OUTLINE` section at the very top under `# CONTEXT`. This is the **only part you should edit.** Everything else must remain untouched.

Replace the following fields:

* `[SUBJECT_NAME_HERE]` — your subject name
* `Undergraduate — B.Tech` — adjust your course level if it differs
* The content between `<your_input_start>` and `<your_input_end>` — your module syllabus

Remove the delimiter tags themselves before submitting. Your input should look like this:

```markdown
M{num}: {module_name}
* {concept_name}
  * {sub_concept_name}
    * {nested_further_sub_concept_name}
* {concept_name}
  * {sub_concept_name}
```

The indentation is meaningful — it tells the AI what is a topic, what is a subtopic, and what is nested inside what. Preserve it carefully.

{% hint style="success" icon="image" %}
#### Optionally include image links

If your syllabus topic has a reference diagram or image you want embedded, add its URL inline next to the topic name using the notation shown in the prompt:

```
M{num}: {module_name}
* {concept_name}
  * {sub_concept_name}[optional-image_link]
    * {nested_further_sub_concept_name}[optional-image_link]
* {concept_name}
  * {sub_concept_name}[optional-image_link]
```

Images are supported in both output formats.

* For Multiple Images:
  * If a topic has multiple images, list them comma-separated within the same bracket: `* Subtopic: [image_url_1 , image_url_2 , image_url_3]` — the AI will embed each image in sequence at that topic's position.



**NOTE:** _Before adding any image URL to the prompt, verify it manually — paste the URL directly into a browser tab and confirm it opens as a visible image in the browser itself. A valid URL renders the image inline in the browser tab. Reject the URL if it triggers a file download, requires a login, returns an error page, or points to a local file path. Only publicly accessible, directly renderable image URLs are valid._
{% endhint %}

{% hint style="danger" %}
#### One Module at a Time

* Do not paste multiple modules into a single run.&#x20;
* One module per prompt produces focused, deep, high-quality notes.&#x20;
* Adding more than one module degrades depth, length, and coherence significantly.
{% endhint %}

At this Point, You're ready to Send it to AGENT.

<p align="center"><a class="button primary" data-icon="paper-plane">SEND to AGENT</a></p>
{% endstep %}

{% step %}
### Answer the pre-flight questions

Before generating anything, the AI will ask you two questions:

* **Depth**
  * Lean
  * Balanced
  * Extreme Deep
* **Output format**
  * GFM Markdown
  * HTML

<p align="center"><a class="button primary" data-icon="paper-plane">SEND to AGENT</a></p>

Answer both questions, then the AI will proceed through all three phases automatically: creating the skeleton, filling every section, and validating that nothing was missed.

#### A Note on AI Token Cost

| Format       | Token Cost | Visual Control | Recommended                            |
| ------------ | ---------- | -------------- | -------------------------------------- |
| GFM Markdown | Low        | Standard       | Yes                                    |
| HTML         | High       | Full           | Only When Styling presentation matters |

**RECOMMENDATIONS:**

* If you are generating notes for personal study, GFM Markdown is the practical choice.&#x20;
* HTML is worth the cost when you need a polished, shareable document.
{% endstep %}

{% step %}
### Saving and Exporting Your Output

#### GFM Markdown output

* Paste into **Notion** or **Obsidian** — both render GFM natively.
  * To export to PDF from there, use the built-in export option in either app.
* Alternatively, paste the raw markdown into [innateblogger.com/p/markdown-to-pdf.html](https://www.innateblogger.com/p/markdown-to-pdf.html), then click the **PRINT** button in the toolbar. Adjust font, margins, column width, and tone from the style panel before printing.

#### HTML output

* The AI produces a self-contained HTML file.
* Open it in any browser, then use **File → Print → Save as PDF**.
  * On **macOS**: use the Print dialog, click the PDF dropdown at the bottom left, select Save as PDF.
  * On **Windows**: select Microsoft Print to PDF as the printer, click Print.
{% endstep %}

{% step %}
### Share What the Agent Makes

If these notes helped you, consider contributing them to **Vaultscapes** (with CREDITS to your name)— so the next batch of juniors can gain directions and thank you as a senior.
{% endstep %}
{% endstepper %}
