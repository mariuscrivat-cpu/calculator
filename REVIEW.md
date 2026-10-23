# Reguli de review

Ordinea contează: o problemă de mai sus e mai gravă decât una de mai jos.

1. **Cerința** (blocant): tichetul e îndeplinit complet, iar diff-ul nu conține nimic în afara scopului lui. Dacă cerința era deja îndeplinită și agentul n-a modificat nimic, e corect.
2. **Teste** (blocant): fiecare funcție nouă sau modificată din diff are teste (noi sau adaptate). Teste existente pot dispărea sau se pot schimba când e justificat de diff: cod înlocuit sau eliminat, refactorizare, parametrizare, mutare. Dacă dispar teste fără legătură cu diff-ul sau fără acoperire echivalentă, e blocant. Contează contextul, nu numărul de teste.
3. **Corectitudine** (blocant dacă e bug real): bug-uri și cazuri limită neacoperite (zero, negative, float, împărțire la zero).
4. **Reutilizare și clean code** (sugestie): nume clare, fără duplicări, funcții mici. Verifică dacă există deja cod care face același lucru.
5. **Optimizare** (sugestie): doar dacă ai o ineficiență reală și poți spune de ce. Altfel nu comenta.

Nu cere schimbări de stil pe cod neatins de diff.
