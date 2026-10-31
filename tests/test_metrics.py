from resume_matchmaker_ml.evaluation.metrics import precision_at_k, recall_at_k, ndcg_at_k

def test_metrics():
    relevant = {"a", "c"}
    ranked = ["a", "b", "c"]
    assert precision_at_k(relevant, ranked, 2) == 0.5
    assert recall_at_k(relevant, ranked, 2) == 0.5
    assert 0 < ndcg_at_k(relevant, ranked, 3) <= 1
