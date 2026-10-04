from pathlib import Path
SOURCE=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text(encoding="utf-8")
def test_surface():
    for name in ["register_tool","request_checkout","report_return","flag_overdue","resolve_quarantine","get_tool","get_tools_page","get_reviews_page","get_summary"]:assert f"def {name}" in SOURCE
def test_consensus_and_recovery():
    for term in ["run_nondet_unsafe","CHECKED_OUT","OVERDUE","QUARANTINED","inspection_rules","now()<=int(t.due_at)"]:assert term in SOURCE
def test_runner():assert SOURCE.startswith('# { "Depends": "py-genlayer:')
