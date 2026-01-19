# TESTPAGE / Gitbook to Shadcn\_flutter

# Recommendations on Gitbook to shadcn_flutter Component Mapping

## Blocks

### Paragraphs
A Block is just text, that’s how it’s represented in Markdown.

### Headings

# I'm a page title
## My heading 1
### My heading 2
#### My heading 3

### Unordered lists

* Item
  * Nested item
    * Another nested item
  * Yet another nested item
* Another item
* Yet another item

### Ordered lists

1. Item 1
   1. Nested item 1.1
      1. Nested item 1.1.1
   2. Nested item 1.2
2. Item 2
3. Item 3

### Task lists

* [ ] Here’s a task that hasn’t been done
  * [x] Here’s a subtask that has been done, indented using `Tab`.
  * [ ] Here’s a subtask that hasn’t been done.
* [ ] Finally, an item, unindented using `shift` + `tab`.

### Hints

{% hint style="info" %}
**Info hints** are great for showing general information, or providing tips and tricks.
{% endhint %}

{% hint style="success" %}
**Success hints** are good for showing positive actions or achievements.
{% endhint %}

{% hint style="warning" %}
**Warning hints** are good for showing important information or non-critical warnings.
{% endhint %}

{% hint style="danger" %}
**Danger hints** are good for highlighting destructive actions or raising attention to critical information.
{% endhint %}

{% hint style="info" %}
**This is a H2 heading**

This is a line

This is an inline <img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F0FzoF68PAY3Rv297meNB%2Fcommand.svg?alt=media&#x26;token=b07ff261-6e28-4879-8ab1-039a49f6ab41" alt="The Apple computer command icon" data-size="line"> image

* This is a second <mark style="color:orange;background-color:purple;">line using an unordered list and color</mark>
  {% endhint %}

### Quotes

> "No human ever steps in the same river twice, for it’s not the same river and they are not the same human." — *Heraclitus*

### Code blocks

{% code title="index.js" overflow="wrap" lineNumbers="true" %}
dart
flutter pub get

{% endcode %}

---

You can also combine code blocks with a 'tabs block' to offer the same code example in multiple different languages:

{% tabs %}
{% tab title="JavaScript" %}
javascript
let greeting = function (name) {
  console.log(`Hello, ${name}!`);
};
greeting("Anna");

{% endtab %}

{% tab title="Ruby" %}
ruby
greeting = lambda {|name| puts "Hello, #{name}!"}
greeting.("Anna")

{% endtab %}

{% tab title="Elixir" %}
elixir
greeting = fn name -> IO.puts("Hello, #{name}!") end
greeting.("Anna")

{% endtab %}
{% endtabs %}

### Files

{% file src="<https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fgit-blob-9ff1c1eef1d9ee1744295e274d3ee01fae848a20%2Fexample.pdf?alt=media>" %}
This is a caption on a file.
{% endfile %}

### Images

<div align="center"><figure><img src="https://images.unsplash.com/photo-1446776709462-d6b525c57bd3?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwyfHxzcGFjZXxlbnwwfHx8fDE3MzMxOTY5NTR8MA&#x26;ixlib=rb-4.0.3&#x26;q=85" alt="A photograph taken from space looking back towards Earth. A satellite is in the foreground, and in the background is an ocean-covered part of our planet with patchy clouds."><figcaption><p>Example of an image block with a caption</p></figcaption></figure></div>

### Embedded URLs

{% embed url="URL_HERE" %}

### Tables

<table data-full-width="false"><thead><tr><th>Company</th><th>Status<select><option value="36bef47f343d4588bc43db3e5c701796" label="In progress" color="blue"></option></select></th><th>Contact</th><th>MRR</th><th data-hidden>Contact</th><th data-hidden>MRR</th><th data-hidden>Status<select><option value="3e7a52c673ec4a01992566d18271f7a5" label="In progress" color="blue"></option><option value="2362fd3eafc7476fb8646ac754f34b72" label="Done" color="blue"></option></select></th></tr></thead><tbody><tr><td><strong>Ace AI</strong> – Design</td><td><span data-option="36bef47f343d4588bc43db3e5c701796">In progress</span></td><td><a href="mailto:noreply@gitbook.com">rena@ace.ai</a></td><td>$450</td><td><a href="mailto:noreply@gitbook.com">rena@ace.ai</a></td><td>$420</td><td><span data-option="3e7a52c673ec4a01992566d18271f7a5">In progress</span></td></tr><tr><td><strong>Discrete Data</strong> – API</td><td></td><td><a href="mailto:noreply@gitbook.com">dave@dd.inc</a></td><td>$100</td><td><a href="mailto:noreply@gitbook.com">dave@dd.inc</a></td><td>$69</td><td></td></tr></tbody></table>

### Cards

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-type="image">Cover image (dark)</th><th data-hidden data-type="image">Cover image (dark)</th><th data-hidden data-card-cover-dark data-type="image">Cover image (dark)</th></tr></thead><tbody><tr><td><strong>GitBook homepage</strong></td><td>Visit our website and find out more about GitBook.</td><td><a href="https://www.gitbook.com/">https://www.gitbook.com/</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHAbAKXyi5SHXH1rDhg4E%2FGitBook%20homepage.png?alt=media&#x26;token=b2ced317-e488-408b-94a2-03bf72cce821">25_12_10_cards_3.png</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYYaAqhyC3yLcBknZdlmW%2FGitBook%20homepage.png?alt=media&#x26;token=8478251c-456e-4f30-8b32-39cbcc5640ef">25_12_10_cards_2.png</a></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYYaAqhyC3yLcBknZdlmW%2FGitBook%20homepage.png?alt=media&#x26;token=8478251c-456e-4f30-8b32-39cbcc5640ef">25_12_10_cards_2.png</a></td></tr><tr><td><strong>Developer docs</strong></td><td>Build you own GitBook integration!</td><td><a href="https://developer.gitbook.com/">https://developer.gitbook.com/</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F1wL4yuiP0Pi9Oeu0wnmm%2FDeveloper%20docs.png?alt=media&#x26;token=95e0440c-530d-4ce8-8910-607902fc563c">25_12_10_cards_1.png</a></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FLpBdK9z1nnfqwZiJxOuD%2FDeveloper%20docs.png?alt=media&#x26;token=32bed668-de47-427b-9371-0cb4ae6976f0">25_12_10_cards.png</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FLpBdK9z1nnfqwZiJxOuD%2FDeveloper%20docs.png?alt=media&#x26;token=32bed668-de47-427b-9371-0cb4ae6976f0">25_12_10_cards.png</a></td></tr><tr><td><strong>Sign up to GitBook</strong></td><td>Click here to get started for free.</td><td><a href="https://app.gitbook.com/join">https://app.gitbook.com/join</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fg2kgdfMsxOpWQx1Meq8s%2FSign%20up.png?alt=media&#x26;token=e7ef635a-1864-4944-b5a9-2ba7893f6cc0">25_12_10_cards_5.png</a></td><td></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fp4zjlQyIPTIdwuCeremo%2FSign%20up.png?alt=media&#x26;token=2b8904a8-917f-4eb1-b5fe-5a5575757376">25_12_10_cards_4.png</a></td></tr></tbody></table>

### Tabs

{% tabs %}
{% tab title="Windows" %}
Here are the instructions for Windows
{% endtab %}

{% tab title="macOS" %}
Here are the instructions for macOS
{% endtab %}

{% tab title="Linux" %}
Here are the instructions for Linux
{% endtab %}
{% endtabs %}

### Expandable

<details>

<summary>Step 1: Start using expandable blocks</summary>

To add an expandable block hit `/` on an empty block, or click the `+` on the left of the editor, and select **Expandable**.

</details>

<details>

<summary>Step 2: Add content to your block</summary>

Once you’ve inserted an expandable block, you can add content to it — including lists and code blocks.

</details>

### Stepper

{% step %}
### Step 1 title
Step 1 text
{% endstep %}
{% step %}
### Step 2 title
Step 2 text
{% endstep %}
{% endstepper %}

### Math & TeX

$$
s = \sqrt{\frac{1}{N-1} \sum\_{i=1}^N (x\_i - \overline{x})^2}
$$

### Page links

{% content-ref url="" %}
[](https://gitbook.com/docs/creating-content/blocks)
{% endcontent-ref %}

{% content-ref url="../formatting/inline" %}
[inline](https://gitbook.com/docs/creating-content/formatting/inline)
{% endcontent-ref %}

### Buttons

<a href="https://app.gitbook.com/join" class="button primary">Sign up to GitBook</a>
<a href="#annotations" class="button secondary">Go to top</a>

### Icons

<i class="fa-facebook">:facebook:</i>
<i class="fa-github">:github:</i>
<i class="fa-x-twitter">:x-twitter:</i>
<i class="fa-instagram">:instagram:</i>

## Markdown editing

### Italic

*Italic*
_Italic_

### Bold

**Bold**
__Bold__

### Links

[Link](http://a.com)

### Images

![Image](http://url/a.png)

### Blockquotes

> Blockquote

### Horizontal rules

---

### Code blocks
```dart
const CodeSnippet(
  code: Text('flutter pub get'),
)
```
