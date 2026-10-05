"""
Section 12: Key Findings
"""
from common import load_math, load_portuguese

mat = load_math()
por = load_portuguese()

print("KEY FINDINGS")
print("1. G1 and G2 are strong numerical indicators of final performance.")
print(f"2. G2-G3 correlation = {mat['G2'].corr(mat['G3']):.3f}")
print(f"3. G1-G3 correlation = {mat['G1'].corr(mat['G3']):.3f}")
print(f"4. Mean G3 for students with zero previous failures = {mat.loc[mat['failures']==0,'G3'].mean():.2f}")
print(f"5. Mean G3 for students with three previous failures = {mat.loc[mat['failures']==3,'G3'].mean():.2f}")
print(f"6. Mathematics mean G3 = {mat['G3'].mean():.2f}")
print(f"7. Portuguese mean G3 = {por['G3'].mean():.2f}")
print("8. Maternal education can be examined through grouped means and correlation.")
print("9. Study time shows a modest association with final grade.")
print("10. Home internet access can be compared using grouped mean G3.")
print("11. High going-out frequency can be examined as a behavioural factor.")
print("12. Correlation shows association, not causation.")
