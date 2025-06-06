---
title: Markdown Demo
icon: material/language-markdown-outline  # sets the header icon
description: "This is a demo of the markdown syntax."  # meta description
tags:
  - Some Tag
  - Some Other Tag
---


!!!Note
    This is a demo of the markdown syntax used in this documentation. It is not
    part of the site.

```python linenums="1"  title="my_file.py"
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400) # (1)!
y = np.sin(x ** 2)
plt.plot(x, y)
plt.show()
```

1. This is a comment in the code block.

## Grid Cards

<div class="grid cards" markdown>

- :octicons-desktop-download-24:{ .lg .middle } **Set up in 5 minutes**

    ---

    Install [`mkdocs-material`]() with [`pip`]() and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started]()

- :fontawesome-brands-markdown:{ .lg .middle } **It's just Markdown**

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference]()

- :material-format-font:{ .lg .middle } **Made to measure**

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization]()

- :material-scale-balance:{ .lg .middle } **Open Source, MIT**

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License]()

</div>

## Subheading

Markdown is a lightweight markup language with plain-text-formatting syntax. Its
design allows it to be converted to many output formats, but the original tool
by the same name only supports HTML. Markdown is often used to format readme
files, for writing messages in online discussion forums, and to create rich text
using a plain text editor.

## Lorem Ipsum

Lorem **ipsum dolor sit amet**, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.

## Tables

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

## Lists

### Unordered

- Item 1
- Item 2
  - Item 2a
  - Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
    1. Item 3a
    1. Item 3b

## Tabs

=== "C"

    ```c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ```c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

## Images

![Random Image](https://picsum.photos/200/300){ width="200" loading="lazy" }

## Links

<http://github.com> - automatic!
[GitHub](http://github.com)

## Blockquotes

As Kanye West said:

> We're living the future so
> the present is our past.

## Inline code

Run the command: `pip install my_package`

## Task Lists

- [x] @mentions, #refs, [links](index.md), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## Emoji

@octocat :+1: This PR looks great - it's ready to merge! :rocket:

## Definition Lists

term
: definition

term2
: definition2

## Strikethrough

~~The world is flat~~

## Heading IDs

### My Great Heading {#custom-id}

## Line Breaks

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a
*separate paragraph*.

This line is also a separate paragraph, but... This line is only separated by a
single newline, so it's a separate line in the *same paragraph*.

## Admonitions

!!! note
    This is a note

!!! tip
    This is a tip

!!! bug
    This is a bug

!!! quote
    This is a quote

!!! example

    ```python title="some_file.py"
    from my_package import my_function
    ```

!!! abstract
    This is an abstract

!!! warning
    This is a warning

!!! danger
    This is a danger

!!! success
    This is a success

!!! question
    This is a question

!!! failure
    This is a failure

!!! info
    This is a info

!!! note "This has a custom title"
    This is a note

!!! note ""
    This one has no title

??? info "Click to expand"
    `???` makes for collapsible content

see docs on [Custom
Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)
for customizing the icon

### Inline Admonitions

(must be declared prior to the block they are next to)

!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.

```markdown
!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.
```

## Keyboard keys

++ctrl+cmd+f++

## Buttons

[Subscribe to our newsletter](index.md){ .md-button .md-button--primary }

with icons

[Send :fontawesome-solid-paper-plane:](index.md){ .md-button }

The goal of this page is to get you up and running quickly with a modern python
repository that you can use to develop and deploy your package.

This guide will create a *new* project directory.

???question "What if I have an existing project?"

    There is no automated way to migrate an existing project to use this
    template.  We recommend creating a new project and copying over your
    existing source code and metadata manually:

    1. Follow the guide below to create a new project (using the same name as
       your existing project).
    2. Copy your existing source code into the new project. For example, if
       your existing project has a `src` directory, copy its contents into
       the new project's `src` directory.  If not, copy your top-level module
       into the new project's `src` directory (then, make sure to update any places
       in your repo that have hard-coded references to the module's path).
    3. Manually copy over the project metadata from your existing project's
       `setup.py`, `setup.cfg`, or `pyproject.tom` into the new `[project]` table
       of your new `pyproject.toml`.  If you use setuptools, their
       [Quickstart docs](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
       have good examples of metadata in each file format.
    4. From there, it will depend on your project structure & complexity.  You
       may need to manually copy over other files, such as `requirements.txt`,
       `requirements-dev.txt`, `Makefile`, etc.  You may also need to manually
       update your CI config files to use the new project structure.

## Install Copier

First install [Copier](https://copier.readthedocs.io/en/stable/),
which we will use to run the project template.

<div class="termy">

```console
$ pip install copier
---> 100%
Successfully installed copier
```

</div>

!!!note
    This will install Copier in your current Python environment. If you use
    conda, make sure to `conda activate` the environment you want to use prior
    to installing Copier. (It can be any environment... we're only going to
    use copier once to create a new project.)

## Create a project

Next, run the following command to create a new project from the
[pydev-guide template](https://github.com/pydev-guide/pyrepo-copier).
Replace `<project-name>` with the desired path to your project, this
will be the name of the directory that will be created.

```bash
copier copy gh:pydev-guide/pyrepo-copier <project-name>
```

### Select a Mode

You will first be asked to select a "mode":

<div class="termy">

```console
$ copier copy gh:pydev-guide/pyrepo-copier my-project

// To opt in to the default tooling, press Enter.
// Use "Simple" for minimal tooling, or "Customize" to ask questions.

<font><b>🎤 Welcome! Please select a mode:</b></font>
<font>   (use arrow keys)</font>
<font color='#FFAF00'>  ≫ ✨ Fully featured - default tooling</font>
<font>    📦 Simple package - minimal tooling</font>
<font>    🙋‍♀️ Customize - ask me questions</font>
```

</div>

## Post-Generation Tasks

After the project is generated, you will need to do a few things to get it
ready for development.
