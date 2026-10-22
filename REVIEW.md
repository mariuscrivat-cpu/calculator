# Reguli de review

Ordinea contează: o problemă de mai sus e mai gravă decât una de mai jos.

1. **Cerința** (blocant): tichetul e îndeplinit complet, iar diff-ul nu conține nimic în afara scopului lui. Dacă cerința era deja îndeplinită și agentul n-a modificat nimic, e corect.
2. **Teste** (blocant): orice comportament nou are teste noi sau adaptate. Niciun test existent nu e șters sau redenumit, decât dacă tichetul cere asta explicit.
3. **Corectitudine** (blocant dacă e bug real): bug-uri și cazuri limită neacoperite (zero, negative, float, împărțire la zero).
4. **Reutilizare și clean code** (sugestie): nume clare, fără duplicări, funcții mici. Verifică dacă există deja cod care face același lucru.
5. **Optimizare** (sugestie): doar dacă ai o ineficiență reală și poți spune de ce. Altfel nu comenta.

Nu cere schimbări de stil pe cod neatins de diff.
