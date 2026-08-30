# Cross-platform podcast example

Use the user's approved browser or connector for the chosen audio-generation
service. A generic successful path is:

```text
approved browser or connector
-> upload the verified course source pack and producer brief
-> choose the requested format and length
-> generate one version
-> download
-> verify duration and complete decoding
-> audit the transcript or full audio
-> copy to the user-approved destination and compare hashes
```

Keep pronunciation decisions in the project instead of a global personal file.
For technical material, spell out acronyms when ambiguity is likely and do not
read underscores or code punctuation literally.

Recommended project files:

```text
podcast-project/
|-- sources/course-source-pack.md
|-- production/producer-brief.md
|-- production/focused-prompt.txt
|-- output/episode.m4a
|-- qa/transcript-or-timestamp-audit.md
`-- delivery/                 Optional user-requested copy
```

Do not place a learner's name, school account, local home path, private course
files, quiz wording, answer keys, or assignment solutions in a public example.
Never overwrite an existing episode unless the user explicitly requests it.
