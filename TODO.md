# To-do

- [x] check and remove XML markup
- [x] add context-UUID
- [x] remove duplicates
- [x] develop ArangoDB upload tool (mltb2)
- [x] upload to ArangoDB
- [x] add new OpenAI wrapper
- [x] create different prompts
  - question
  - imperative
- [x] develop ArangoDB script
- [x] run and monitor ArangoDB script
- [ ] download from ArangoDB
- [ ] unpack questions and check results
- [ ] add question-UUID
- [ ] remove duplicate questions
- [ ] remove contexts without questions

## Issues

- question like this are an issue (not specific enough):

```text
1. Wo wurde Samuele Romanin geboren?
2. Was war sein Beruf?
3. Mit wem zog Samuele nach Venedig?
4. Wer unterstützte ihn bei seinen Arbeiten?

1. Wo studierte Hoekstra Biologie?
2. Wann wurde sie promoviert?
3. Wo war sie Post-Doktorandin?
4. Was untersucht sie?
```

- conclusion: we use no no short questions, only long questions
