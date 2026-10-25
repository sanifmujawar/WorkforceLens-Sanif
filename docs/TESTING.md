# WorkforceLens verification

Checked 25 October 2026 using Python 3.12.8 and the pinned requirements in the existing local validation environment. A separate environment install was not repeated.

`python -m pytest -q`: four current-version tests passed. They check known synthetic standardised rates and weights, exclusion of missing and small cells, no eligible overlap, and Streamlit execution with both stratification choices. The first app-test attempt used an incorrectly relative path; it was corrected to an absolute repository entrypoint path before the successful run.

Current source results are stored in results.json. No hosted deployment, current-version mobile/accessibility audit, independent participants, external assessment approval or student-understanding confirmation is claimed. RetainWise records under inherited/ are historical upstream evidence, not WorkforceLens verification.
