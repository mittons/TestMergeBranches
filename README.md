# TestMergeBranches

### **Welcome to the TestMergeBranches Repository!**

## Table of Contents
- [About Project](#about-project)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [Appendix - Description of Project](#appendix---description-of-project)

## About Project
This is a project meant to test different methods of merging branches to see which works best for my current context.

## License
This project is licensed under the [UNLICENSE LICENSE](LICENSE) - see the file for details.

## Acknowledgements
- **ChatGPT**: Powered by OpenAI, specifically ChatGPT-4. The main files in this project are human-generated content, with additional content ranging between human- and AI-generated. Definitions of key terms like 'Content', among other definitions, are available on [The OpenAI Terms of Service page](https://openai.com/policies/terms-of-use#using-our-services).
- <details>
    <summary>Click to expand/collapse further details!</summary>
    &nbsp; 

    Essentially, the entire project, except for the Appendix and its related data, was human-generated.
    - The introductory text of the Appendix is completely AI-generated, based entirely on human input, and was created after the more detailed section of the Appendix.
    - The detailed section of the Appendix was completely human-generated. Some intermediate steps were entirely AI-generated. [See Raw State Description Data Index](version_2_ai_refined_code/raw_data/README.md).
    - The scripts for generating the detailed section of the Appendix were initially human-generated, in collaboration with AI. [See folder with human-generated scripts](generate_state_description_scripts/version_1_quick_n_dirty_human_code).
    - Post-execution, these scripts were refined with AI assistance, turning them into AI-generated content. [See folder with AI-refined scripts](generate_state_description_scripts/version_1_quick_n_dirty_human_code).
    - Bottom line: Collaboration with other entities that provide service, whether human or AI, is amazing, beneficial, and enriching!
    </details>
    &nbsp; 

*Current version of this Acknowledgements section is powered by ChatGPT-4 in collaboration with the owner of this repository.*


## Contact
Axel Gauti Guðmundsson - [@axelgauti](https://twitter.com/axelgauti) - axel@axelgauti.is


## Appendix - Description of Project

### Description of Appendix Contents:

In this appendix, we delve into the intricacies of the project's evolution, focusing on the transition and transformation of data across branches during development. The visual representations here are designed to elucidate the following key aspects:

1. **Initial State and Checkout Process**: Starting with Commit A, we illustrate the initial state of the `main` branch and how it translates into the `staging` branch upon checkout.

2. **Staging Branch Commits**: The progression from Commit B through Commit G on the `staging` branch demonstrates incremental changes, including additions and removals (notably, the disappearance of data in folders D and E in Commit F).

3. **Squash Merges and Data Integration**: Critical transitions are showcased in the 'After Squash Merge onto main' sections (up to Commit G and later N). These sections highlight how multiple changes from `staging` are consolidated into single commits on `main`, effectively transferring the accumulated data changes up to that point.

4. **Commit Reiterations**: To reinforce understanding, certain patterns are repeated, such as the transition from Commit N on `staging` to its integration into `main`, mirroring the earlier process with Commit G.

### Appendix Contents - Visualization of State Changes in the Repository:

<details open>
<summary>Commit A (on main)</summary>

```
main    (Data):     A
------------------ ---
main    (History):  A
                    
staging (History):  
------------------ ---
staging (Data):     
```

</details>

<details open>
<summary>Checkout A (to staging, from main branch)</summary>

```
main    (Data):     A
------------------ ---
main    (History):  A
                    |
staging (History):  \
------------------ ---
staging (Data):     A
```

</details>

<details open>
<summary>Commit B (on staging)</summary>

```
main    (Data):     A
------------------ ------
main    (History):  A
                    |
staging (History):  \ - B
------------------ ------
staging (Data):     A | B
```

</details>

<details>
<summary>Commit C (on staging)</summary>

```
main    (Data):     A
------------------ ----------
main    (History):  A
                    |
staging (History):  \ - B - C
------------------ ----------
staging (Data):     A | B | C
```

</details>

<details>
<summary>Commit D (on staging)</summary>

```
main    (Data):     A
------------------ --------------
main    (History):  A
                    |
staging (History):  \ - B - C - D
------------------ --------------
staging (Data):     A | B | C | D
```

</details>

<details open>
<summary>Commit E (on staging)</summary>

```
main    (Data):     A
------------------ ------------------
main    (History):  A
                    |
staging (History):  \ - B - C - D - E
------------------ ------------------
staging (Data):     A | B | C | D | E
```

</details>

<details open>
<summary>Commit F (on staging, removed D and E folders)</summary>

```
main    (Data):     A
------------------ ----------------------
main    (History):  A
                    |
staging (History):  \ - B - C - D - E - F
------------------ ----------------------
staging (Data):     A | B | C |       | F
```

</details>

<details open>
<summary>Commit G (on staging)</summary>

```
main    (Data):     A
------------------ --------------------------
main    (History):  A
                    |
staging (History):  \ - B - C - D - E - F - G
------------------ --------------------------
staging (Data):     A | B | C |       | F | G
```

</details>

<details open>
<summary>After Squash Merge onto main (up to Commit G)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ --------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G
------------------ --------------------------
staging (Data):     A | B | C |       | F | G
```

</details>

<details>
<summary>Commit H (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H
------------------ ------------------------------
staging (Data):     A | B | C |       | F | G | H
```

</details>

<details>
<summary>Commit H (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H
------------------ ------------------------------
staging (Data):     A | B | C |       | F | G | H
```

</details>

<details>
<summary>Commit I (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ----------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I
------------------ ----------------------------------
staging (Data):     A | B | C |       | F | G | H | I
```

</details>

<details>
<summary>Commit J (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ --------------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I - J
------------------ --------------------------------------
staging (Data):     A | B | C |       | F | G | H | I | J
```

</details>

<details>
<summary>Commit K (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ------------------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K
------------------ ------------------------------------------
staging (Data):     A | B | C |       | F | G | H | I | J | K
```

</details>

<details>
<summary>Commit L (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ----------------------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L
------------------ ----------------------------------------------
staging (Data):     A | B | C |       | F | G | H | I | J | K | L
```

</details>

<details>
<summary>Commit M (on staging, removed H and K folders`)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ --------------------------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L - M
------------------ --------------------------------------------------
staging (Data):     A | B | C |       | F | G |   | I | J |   | L | M
```

</details>

<details open>
<summary>Commit N (on staging`)</summary>

```
main    (Data):     A | B | C |       | F | G
------------------ ------------------------------------------------------
main    (History):  A                       G
                    |                       |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L - M - N
------------------ ------------------------------------------------------
staging (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N
```

</details>

<details open>
<summary>After Squash Merge onto main (up to Commit N)</summary>

```
main    (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N
------------------ ------------------------------------------------------
main    (History):  A                       G                           N
                    |                       |                           |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L - M - N
------------------ ------------------------------------------------------
staging (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N
```

</details>

<details>
<summary>Commit O (on staging)</summary>

```
main    (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N
------------------ ----------------------------------------------------------
main    (History):  A                       G                           N
                    |                       |                           |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L - M - N - O
------------------ ----------------------------------------------------------
staging (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N | O
```

</details>

<details>
<summary>After Squash Merge onto main (up to Commit O)</summary>

```
main    (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N | O
------------------ ----------------------------------------------------------
main    (History):  A                       G                           N   O
                    |                       |                           |   |
staging (History):  \ - B - C - D - E - F - G - H - I - J - K - L - M - N - O
------------------ ----------------------------------------------------------
staging (Data):     A | B | C |       | F | G |   | I | J |   | L | M | N | O
```

</details>

