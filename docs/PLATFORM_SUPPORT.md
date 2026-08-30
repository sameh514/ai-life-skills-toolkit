# Platform support

## Cross-platform baseline

The core installer and private vault use Python and `pathlib`, with no hard-coded
Windows or macOS home path. Python 3.10 or newer is recommended.

The full validation and installer test suite runs successfully on GitHub-hosted
Windows and macOS systems. Both platforms install the same eight everyday
skills.

## Common optional dependencies

Different skills need different tools:

| Capability | Typical dependency |
|---|---|
| PDF rendering and inspection | Poppler, `pypdf`, `reportlab` |
| PowerPoint generation | Python presentation libraries or an approved presentation tool |
| Study-podcast generation | The user-approved audio service and browser or connector |
| Encrypted profile vault | Python package `cryptography` |

Install only the dependencies required by the skill being used.

## Browser handoffs

`use-preferred-browser` works with the user's stated browser on either platform.
It does not assume that Chrome, Edge, Firefox, or Safari is acceptable merely
because automation exists there.

## Windows notes

- Use `py` instead of `python` if required by the Python launcher.
- Store private files inside the current Windows user profile and enable
  BitLocker or device encryption when available.

## macOS notes

- The vault applies file mode `0600` after each write.
- FileVault protects data at rest when the computer is powered off or locked.
