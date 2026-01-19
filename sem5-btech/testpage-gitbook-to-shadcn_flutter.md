# TESTPAGE / Gitbook to Shadcn\_flutter

# Recommendations on Gitbook to shadcn_flutter Component Mapping

This document shall aim to define the standard mapping strategy between Gitbook markdown blocks and their corresponding shadcn_flutter widget implementations for the Vaultscapes application.

## Overview

When fetching content from Gitbook pages (via `.md` suffix URLs), the raw markdown content needs to be parsed and converted into Flutter widgets using shadcn_flutter components. This ensures a consistent, native-looking UI while preserving the semantic meaning of the original content.

Here are some recommendations on conversion of gitbook content into respective flutter widget using shadcn_flutter package, you can brainstorm on those which are not yet covered by developer by looking into the shadcn_flutter documentation queried from context7 MCP Server.

---

## Blocks

### Paragraphs
**Gitbook Syntax:**
```markdown
Because a paragraph block is just text, that’s how it’s represented in Markdown.
```

**shadcn_flutter Implementation:**
```dart
const Text('Paragraph').p
```

### Headings
**Gitbook Syntax:**
```markdown
# I'm a page title
## My heading 1
### My heading 2
#### My heading 3
```

**shadcn_flutter Implementation:**
```dart
const Text('Headline 1').h1
const Text('Headline 2').h2
const Text('Headline 3').h3
const Text('Headline 4').h4
```

### Unordered lists
**Gitbook Syntax:**
```markdown
* Item
  * Nested item
    * Another nested item
  * Yet another nested item
* Another item
* Yet another item
```

**shadcn_flutter Implementation:**
```dart
Column(
  crossAxisAlignment: CrossAxisAlignment.start,
  children: [
    const Text('List item 1').li,
    Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text('Nested list:'),
        const Text('Nested list item 1').li,
        const Text('Nested list item 2').li,
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Nested list:'),
            const Text('Nested list item 1').li,
            const Text('Nested list item 2').li,
          ],
        ).li,
      ],
    ).li,
    const Text('List item 3').li,
  ],
)
```

### Ordered lists
**Gitbook Syntax:**
```markdown
1. Item 1
   1. Nested item 1.1
      1. Nested item 1.1.1
   2. Nested item 1.2
2. Item 2
3. Item 3
```

**shadcn_flutter Implementation:**
```dart
Column(
  crossAxisAlignment: CrossAxisAlignment.start,
  children: [
    Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text('1.').muted(),
        const SizedBox(width: 16),
        const Text('List item 1'),
      ],
    ),
    Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('2.').muted(),
            const SizedBox(width: 16),
            const Text('Nested list:'),
          ],
        ),
        Padding(
          padding: const EdgeInsets.only(left: 32),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text('1.').muted(),
                  const SizedBox(width: 16),
                  const Text('Nested list item 1'),
                ],
              ),
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text('2.').muted(),
                  const SizedBox(width: 16),
                  const Text('Nested list item 2'),
                ],
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('3.').muted(),
                      const SizedBox(width: 16),
                      const Text('Nested list:'),
                    ],
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 32),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('1.').muted(),
                            const SizedBox(width: 16),
                            const Text('Nested list item 1'),
                          ],
                        ),
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('2.').muted(),
                            const SizedBox(width: 16),
                            const Text('Nested list item 2'),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ],
    ),
    Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text('3.').muted(),
        const SizedBox(width: 16),
        const Text('List item 3'),
      ],
    ),
  ],
)
```

### Task lists
**Gitbook Syntax:**
```markdown
* [ ] Here’s a task that hasn’t been done
  * [x] Here’s a subtask that has been done, indented using `Tab`.
  * [ ] Here’s a subtask that hasn’t been done.
* [ ] Finally, an item, unindented using `shift` + `tab`.
```

**shadcn_flutter Implementation:**
```dart
// Start unchecked; toggle when the user taps the control.
CheckboxState _state = CheckboxState.unchecked;
@override
Widget build(BuildContext context) {
  return Checkbox(
    state: _state,
    onChanged: (value) {
      setState(() {
        _state = value;
      });
    },
    // Optional label placed on the trailing side.
    trailing: const Text('Remember me'),
  );
}
```

### Hints
**Gitbook Syntax:**
```markdown
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
```

**shadcn_flutter Implementation:**
```dart
const Alert(
  title: Text('Alert title'),
  content: Text('This is alert content.'),
  leading: Icon(Icons.info_outline),
)
const Alert.destructive(
  title: Text('Alert title'),
  content: Text('This is alert content.'),
  trailing: Icon(Icons.dangerous_outlined),
)
```

### Quotes
**Gitbook Syntax:**
```markdown
> "No human ever steps in the same river twice, for it’s not the same river and they are not the same human." — *Heraclitus*
```

**shadcn_flutter Implementation:**
```dart
const Text('Blockquote').blockQuote
```

### Code blocks
**Gitbook Syntax:**
```markdown
{% code title="index.js" overflow="wrap" lineNumbers="true" %}

```dart
flutter pub get
```

{% endcode %}

---

You can also combine code blocks with a 'tabs block' to offer the same code example in multiple different languages:

{% tabs %}
{% tab title="JavaScript" %}

```javascript
let greeting = function (name) {
  console.log(`Hello, ${name}!`);
};
greeting("Anna");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
greeting = lambda {|name| puts "Hello, #{name}!"}
greeting.("Anna")
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
greeting = fn name -> IO.puts("Hello, #{name}!") end
greeting.("Anna")
```

{% endtab %}
{% endtabs %}
```

**shadcn_flutter Implementation:**
```dart
const CodeSnippet(
  code: Text('flutter pub get'),
)
```

### Files
**Gitbook Syntax:**
```markdown
{% file src="<https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fgit-blob-9ff1c1eef1d9ee1744295e274d3ee01fae848a20%2Fexample.pdf?alt=media>" %}
This is a caption on a file.
{% endfile %}
```

**shadcn_flutter Implementation:**
```dart
GestureDetector(
  onTap: () {
    // Handle download logic here
  },
  child: Card(
    padding: const EdgeInsets.all(24),
    child: Row(
      children: [
        Icon(LucideIcons.file, size: 40),
        const SizedBox(width: 16),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('document.pdf').semiBold(),
              const SizedBox(height: 4),
              const Text('2.4 MB • PDF').muted().small(),
            ],
          ),
        ),
        const Icon(LucideIcons.download, size: 28),
      ],
    ),
  ).intrinsic(),
)
```

### Images
**Gitbook Syntax:**
```markdown
<div align="center"><figure><img src="https://images.unsplash.com/photo-1446776709462-d6b525c57bd3?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwyfHxzcGFjZXxlbnwwfHx8fDE3MzMxOTY5NTR8MA&#x26;ixlib=rb-4.0.3&#x26;q=85" alt="A photograph taken from space looking back towards Earth. A satellite is in the foreground, and in the background is an ocean-covered part of our planet with patchy clouds."><figcaption><p>Example of an image block with a caption</p></figcaption></figure></div>
```

**shadcn_flutter Implementation:**
```dart
Image.network('https://flutter.github.io/assets-for-api-docs/assets/widgets/owl-2.jpg')
```

### Embedded URLs
**Gitbook Syntax:**
```markdown
{% embed url="URL_HERE" %}
```

**shadcn_flutter Implementation:**
```dart
We would like to embed web URL content in flutter to display properly as a small fragment not a complete screen, if it's google docs or slides or drive URL then I want a document size aspect ratio of container and if it's a youtube URL then i want a 16:9 horizontal small aspect ratio and if it's just any other URL taking user to external webpage then only the webpage name and icon as woud display an embed is suffice and clicking on it shall open a browser within app with requested URL with option to close it.
```

### Tables
**Gitbook Syntax:**

<table data-full-width="false"><thead><tr><th>Company</th><th>Status<select><option value="36bef47f343d4588bc43db3e5c701796" label="In progress" color="blue"></option></select></th><th>Contact</th><th>MRR</th><th data-hidden>Contact</th><th data-hidden>MRR</th><th data-hidden>Status<select><option value="3e7a52c673ec4a01992566d18271f7a5" label="In progress" color="blue"></option><option value="2362fd3eafc7476fb8646ac754f34b72" label="Done" color="blue"></option></select></th></tr></thead><tbody><tr><td><strong>Ace AI</strong> – Design</td><td><span data-option="36bef47f343d4588bc43db3e5c701796">In progress</span></td><td><a href="mailto:noreply@gitbook.com">rena@ace.ai</a></td><td>$450</td><td><a href="mailto:noreply@gitbook.com">rena@ace.ai</a></td><td>$420</td><td><span data-option="3e7a52c673ec4a01992566d18271f7a5">In progress</span></td></tr><tr><td><strong>Discrete Data</strong> – API</td><td></td><td><a href="mailto:noreply@gitbook.com">dave@dd.inc</a></td><td>$100</td><td><a href="mailto:noreply@gitbook.com">dave@dd.inc</a></td><td>$69</td><td></td></tr></tbody></table>


**shadcn_flutter Implementation:**
```dart
// Builds a bordered cell; amounts can be right-aligned by passing true.
TableCell buildCell(String text, [bool alignRight = false]) {
  final theme = Theme.of(context);
  return TableCell(
    theme: TableCellTheme(
      border: WidgetStatePropertyAll(
        Border.all(
          color: theme.colorScheme.border,
          strokeAlign: BorderSide.strokeAlignCenter,
        ),
      ),
    ),
    child: Container(
      padding: const EdgeInsets.all(8),
      alignment: alignRight ? Alignment.topRight : null,
      child: Text(text),
    ),
  );
}

@override
Widget build(BuildContext context) {
  return ScrollConfiguration(
    behavior: ScrollConfiguration.of(context).copyWith(
      dragDevices: {
        PointerDeviceKind.touch,
        PointerDeviceKind.mouse,
        PointerDeviceKind.trackpad,
      },
      // Disable overscroll glow and bouncing to keep the table steady.
      overscroll: false,
    ),
    child: SizedBox(
      height: 400,
      child: OutlinedContainer(
        child: ScrollableClient(
            // Allow simultaneous horizontal and vertical drags for panning.
            diagonalDragBehavior: DiagonalDragBehavior.free,
            builder: (context, offset, viewportSize, child) {
              return Table(
                // Hook the table's scroll offsets to the ScrollableClient.
                horizontalOffset: offset.dx,
                verticalOffset: offset.dy,
                // The viewport tells the table how much content area is visible.
                viewportSize: viewportSize,
                // Fixed sizes for consistent cell dimensions.
                defaultColumnWidth: const FixedTableSize(150),
                defaultRowHeight: const FixedTableSize(40),
                // Freeze the first and fourth rows, and the first and third columns.
                // These rows/columns stay pinned while the rest scrolls.
                frozenCells: const FrozenTableData(
                  frozenRows: [
                    TableRef(0),
                    TableRef(3),
                  ],
                  frozenColumns: [
                    TableRef(0),
                    TableRef(2),
                  ],
                ),
                rows: [
                  TableHeader(
                    cells: [
                      buildCell('Invoice'),
                      buildCell('Status'),
                      buildCell('Method'),
                      buildCell('Amount', true),
                      buildCell('Verification'),
                      buildCell('Last Updated'),
                    ],
                  ),
                  TableRow(
                    cells: [
                      buildCell('INV001'),
                      buildCell('Paid'),
                      buildCell('Credit Card'),
                      buildCell('\$250.00', true),
                      buildCell('Verified'),
                      buildCell('2 hours ago'),
                    ],
                  ),
                  TableRow(
                    cells: [
                      buildCell('INV002'),
                      buildCell('Pending'),
                      buildCell('PayPal'),
                      buildCell('\$150.00', true),
                      buildCell('Pending'),
                      buildCell('1 day ago'),
                    ],
                  ),
                  TableRow(
                    cells: [
                      buildCell('INV003'),
                      buildCell('Unpaid'),
                      buildCell('Bank Transfer'),
                      buildCell('\$350.00', true),
                      buildCell('Unverified'),
                      buildCell('1 week ago'),
                    ],
                  ),
                ],
              );
            }),
      ),
    ),
  );
}

```

### Cards
**Gitbook Syntax:**

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-type="image">Cover image (dark)</th><th data-hidden data-type="image">Cover image (dark)</th><th data-hidden data-card-cover-dark data-type="image">Cover image (dark)</th></tr></thead><tbody><tr><td><strong>GitBook homepage</strong></td><td>Visit our website and find out more about GitBook.</td><td><a href="https://www.gitbook.com/">https://www.gitbook.com/</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHAbAKXyi5SHXH1rDhg4E%2FGitBook%20homepage.png?alt=media&#x26;token=b2ced317-e488-408b-94a2-03bf72cce821">25_12_10_cards_3.png</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYYaAqhyC3yLcBknZdlmW%2FGitBook%20homepage.png?alt=media&#x26;token=8478251c-456e-4f30-8b32-39cbcc5640ef">25_12_10_cards_2.png</a></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYYaAqhyC3yLcBknZdlmW%2FGitBook%20homepage.png?alt=media&#x26;token=8478251c-456e-4f30-8b32-39cbcc5640ef">25_12_10_cards_2.png</a></td></tr><tr><td><strong>Developer docs</strong></td><td>Build you own GitBook integration!</td><td><a href="https://developer.gitbook.com/">https://developer.gitbook.com/</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F1wL4yuiP0Pi9Oeu0wnmm%2FDeveloper%20docs.png?alt=media&#x26;token=95e0440c-530d-4ce8-8910-607902fc563c">25_12_10_cards_1.png</a></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FLpBdK9z1nnfqwZiJxOuD%2FDeveloper%20docs.png?alt=media&#x26;token=32bed668-de47-427b-9371-0cb4ae6976f0">25_12_10_cards.png</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FLpBdK9z1nnfqwZiJxOuD%2FDeveloper%20docs.png?alt=media&#x26;token=32bed668-de47-427b-9371-0cb4ae6976f0">25_12_10_cards.png</a></td></tr><tr><td><strong>Sign up to GitBook</strong></td><td>Click here to get started for free.</td><td><a href="https://app.gitbook.com/join">https://app.gitbook.com/join</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fg2kgdfMsxOpWQx1Meq8s%2FSign%20up.png?alt=media&#x26;token=e7ef635a-1864-4944-b5a9-2ba7893f6cc0">25_12_10_cards_5.png</a></td><td></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fp4zjlQyIPTIdwuCeremo%2FSign%20up.png?alt=media&#x26;token=2b8904a8-917f-4eb1-b5fe-5a5575757376">25_12_10_cards_4.png</a></td></tr></tbody></table>


**shadcn_flutter Implementation:**
```dart
ScrollConfiguration(
  behavior: ScrollConfiguration.of(context).copyWith(
    dragDevices: {
      PointerDeviceKind.touch,
      PointerDeviceKind.mouse,
    },
  ),
  child: SingleChildScrollView(
    scrollDirection: Axis.horizontal,
    child: IntrinsicHeight(
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisSize: MainAxisSize.min,
        children: [
          for (int i = 0; i < 10; i++)
            CardImage(
              // Simple interaction: open a dialog on tap.
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      title: const Text('Card Image'),
                      content: const Text('You clicked on a card image.'),
                      actions: [
                        PrimaryButton(
                          onPressed: () {
                            Navigator.of(context).pop();
                          },
                          child: const Text('Close'),
                        ),
                      ],
                    );
                  },
                );
              },
              // Network image; replace with your own provider as needed.
              image: Image.network(
                'https://picsum.photos/200/300',
              ),
              // Title and subtitle appear over the image.
              title: Text('Card Number ${i + 1}'),
              subtitle: const Text('Lorem ipsum dolor sit amet'),
            ),
        ],
      ).gap(8),
    ),
  ),
)
```

### Tabs
**Gitbook Syntax:**
```markdown
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
```

**shadcn_flutter Implementation:**
```dart
int index = 0;
@override
Widget build(BuildContext context) {
  return Column(
    children: [
      Tabs(
        // Bind the active tab index; Tabs is the header-only control.
        index: index,
        children: const [
          TabItem(child: Text('Tab 1')),
          TabItem(child: Text('Tab 2')),
          TabItem(child: Text('Tab 3')),
        ],
        onChanged: (int value) {
          // Keep header and body in sync by updating state.
          setState(() {
            index = value;
          });
        },
      ),
      const Gap(8),
      // The IndexedStack acts as the tab body; it switches content by index
      // without unmounting inactive children.
      IndexedStack(
        index: index,
        children: const [
          NumberedContainer(
            index: 1,
          ),
          NumberedContainer(
            index: 2,
          ),
          NumberedContainer(
            index: 3,
          ),
        ],
      ).sized(height: 300),
    ],
  );
}
```


### Expandable
**Gitbook Syntax:**
```markdown
<details>

<summary>Step 1: Start using expandable blocks</summary>

To add an expandable block hit `/` on an empty block, or click the `+` on the left of the editor, and select **Expandable**.

</details>

<details>

<summary>Step 2: Add content to your block</summary>

Once you’ve inserted an expandable block, you can add content to it — including lists and code blocks.

</details>
```

**shadcn_flutter Implementation:**
```dart
const Accordion(
  items: [
    // Item 1: Demonstrates a basic trigger and a longer content body.
    AccordionItem(
      trigger: AccordionTrigger(child: Text('Lorem ipsum dolor sit amet')),
      content: Text(
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
          'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
          'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
          'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
          'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
    ),
    // Item 2: Another entry with its own header and body.
    AccordionItem(
      trigger: AccordionTrigger(
          child: Text(
              'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')),
      content: Text(
          'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
          'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
          'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
          'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
    ),
    // Item 3: A third example to show multiple items expand independently.
    AccordionItem(
      trigger: AccordionTrigger(
          child: Text(
              'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')),
      content: Text(
          'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
          'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
          'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
    ),
  ],
)
```

### Stepper
**Gitbook Syntax:**
{% stepper %}
{% step %}
### Step 1 title
Step 1 text
{% endstep %}
{% step %}
### Step 2 title
Step 2 text
{% endstep %}
{% endstepper %}

**shadcn_flutter Implementation:**
```dart
const Steps(
  // Static steps list with titles and supporting content lines.
  children: [
    StepItem(
      title: Text('Create a project'),
      content: [
        Text('Create a new project in the project manager.'),
        Text('Add the required files to the project.'),
      ],
    ),
    StepItem(
      title: Text('Add dependencies'),
      content: [
        Text('Add the required dependencies to the project.'),
      ],
    ),
    StepItem(
      title: Text('Run the project'),
      content: [
        Text('Run the project in the project manager.'),
      ],
    ),
  ],
)
```

### Math & TeX
**Gitbook Syntax:**
```markdown
$$
s = \sqrt{\frac{1}{N-1} \sum\_{i=1}^N (x\_i - \overline{x})^2}
$$
```

**shadcn_flutter Implementation:**
```dart
Math.tex(
  r'f(x) = x * e^{2 \pi i \xi x}',
  textStyle: theme.typography.p,
)
```

### Page links
**Gitbook Syntax:**
```markdown
{% content-ref url="" %}
[](https://gitbook.com/docs/creating-content/blocks)
{% endcontent-ref %}

{% content-ref url="../formatting/inline" %}
[inline](https://gitbook.com/docs/creating-content/formatting/inline)
{% endcontent-ref %}
```

**shadcn_flutter Implementation:**
```dart
Identify the URL it is taking to if it maps to a subject (see navigation.json) then Internal links should navigate within the app to the respected content; external links open in browser.
```

### Buttons
**Gitbook Syntax:**
```markdown
<a href="https://app.gitbook.com/join" class="button primary">Sign up to GitBook</a>
<a href="#annotations" class="button secondary">Go to top</a>
```

**shadcn_flutter Implementation:**
```dart
PrimaryButton(
  onPressed: () {},
  child: const Text('Primary'),
)
```

### Icons
**Gitbook Syntax:**
```markdown
<i class="fa-facebook">:facebook:</i>
<i class="fa-github">:github:</i>
<i class="fa-x-twitter">:x-twitter:</i>
<i class="fa-instagram">:instagram:</i>
```

**shadcn_flutter Implementation:**
```dart
Icon(RadixIcons.link1)
Icon(BootstrapIcons.link)
Icon(LucideIcons.link)
```

## Markdown editing


### Italic
**Gitbook Syntax:**
```markdown
*Italic*
_Italic_
```

**shadcn_flutter Implementation:**
```dart
style: TextStyle(fontStyle: FontStyle.italic)
```

### Bold
**Gitbook Syntax:**
```markdown
**Bold**
__Bold__
```

**shadcn_flutter Implementation:**
```dart
style: TextStyle(fontStyle: FontStyle.bold)
```

### Links
**Gitbook Syntax:**
```markdown
[Link](http://a.com)
```

**shadcn_flutter Implementation:**
```dart
HoverCard(
  hoverBuilder: (context) {
    // SurfaceCard provides an elevated container with default padding and
    // surface styling. We constrain the width so the text wraps nicely.
    return const SurfaceCard(
      child: Basic(
        leading: FlutterLogo(),
        title: Text('@flutter'),
        content: Text(
            'The Flutter SDK provides the tools to build beautiful apps for mobile, web, and desktop from a single codebase.'),
      ),
    ).sized(width: 300);
  },
  child: LinkButton(
    // The LinkButton acts as the hover target. onPressed is provided for
    // completeness but not used in this example.
    onPressed: () {},
    child: const Text('@flutter'),
  ),
)
```

### Images
**Gitbook Syntax:**
```markdown
![Image](http://url/a.png)
```

**shadcn_flutter Implementation:**
```dart
const Image(
  image: NetworkImage('https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg'),
)
```

### Blockquotes
**Gitbook Syntax:**
```markdown
> Blockquote
```

**shadcn_flutter Implementation:**
```dart
const Text('Blockquote').blockQuote
```

### Horizontal rules
**Gitbook Syntax:**
```markdown
---
```

**shadcn_flutter Implementation:**
```dart
const SizedBox(
  width: 300,
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.stretch,
    children: [
      Text('Item 1'),
      Divider(),
      Text('Item 2'),
      Divider(),
      Text('Item 3'),
    ],
  ),
)
```

### Code blocks
**Gitbook Syntax:**
```markdown
```
flutter pub get
```
```

**shadcn_flutter Implementation:**
```dart
const CodeSnippet(
  code: Text('flutter pub get'),
)
```

---

## Implementation Notes

1. **One Page = One Screen**: Each Gitbook URL should render as a single vertically-scrollable screen.

2. **Dynamic Rendering**: Parse markdown at runtime and build widget tree dynamically.

3. **Caching**: Consider caching parsed content for offline access and performance.

4. **Theme Awareness**: All components should respect the current theme (light/dark mode).

5. **Accessibility**: Ensure proper semantics for screen readers.

6. **Link Handling**: Internal links should navigate within the app; external links open in browser.

---

## Dependencies

Required packages:
- `shadcn_flutter: ^0.0.47` - UI components
- `markdown: ^7.1.1` - Markdown parsing
- `url_launcher: ^6.2.1` - External link handling
- `flutter_math_fork: ^0.7.1` - Math/TeX rendering (optional)
- `cached_network_image: ^3.3.0` - Image caching

---

## Future Enhancements

1. **Syntax Highlighting**: Add code syntax highlighting for code blocks
2. **Offline Support**: Cache rendered content for offline viewing
3. **Search**: Full-text search across all fetched content
