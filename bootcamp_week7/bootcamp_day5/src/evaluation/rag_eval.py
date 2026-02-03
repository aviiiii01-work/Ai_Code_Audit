from typing import List, Dict, Any


def context_match_score(answer: str, contexts: List[str]) -> float:
    answer_words = set(answer.lower().split())
    ctx_words = set(" ".join(contexts).lower().split())
    overlap = answer_words & ctx_words
    return round(len(overlap) / max(len(ctx_words), 1), 2)


def faithfulness_score(answer: str, contexts: List[str]) -> float:
    if not contexts or not answer:
        return 0.0

    context_text = " ".join(contexts).lower()
    answer_words = answer.lower().split()

    overlap = sum(1 for word in answer_words if word in context_text)
    return round(overlap / max(len(answer_words), 1), 2)


def confidence_score(context_score: float, faith_score: float) -> float:
    return round((context_score + faith_score) / 2, 2)


def evaluate_answer(answer: str, contexts: List[str]) -> Dict[str, float]:
    ctx_score = context_match_score(answer, contexts)
    faith_score = faithfulness_score(answer, contexts)
    conf_score = confidence_score(ctx_score, faith_score)

    return {
        "context_match": ctx_score,
        "faithfulness": faith_score,
        "confidence": conf_score
    }


def apply_thresholds(
    evaluation: Dict[str, float],
    thresholds: Dict[str, float]
) -> Dict[str, Any]:

    hallucinated = (
        evaluation["faithfulness"] < thresholds["faithfulness"]
        or evaluation["confidence"] < thresholds["confidence"]
        or (
            "context_match" in thresholds
            and evaluation.get("context_match", 1.0) < thresholds["context_match"]
        )
    )

    evaluation["hallucinated"] = hallucinated
    return evaluation


class SQLRAGEvaluator:

    def evaluate(self, sql: str, rows: List[List[Any]]) -> Dict[str, float]:
        faithfulness = self._faithfulness(sql, rows)
        confidence = self._confidence(sql, rows)

        return {
            "faithfulness": round(faithfulness, 2),
            "confidence": round(confidence, 2)
        }

    def _faithfulness(self, sql: str, rows: List[List[Any]]) -> float:
        if not sql:
            return 0.0

        if not sql.strip().lower().startswith("select"):
            return 0.0

        if rows is None:
            return 0.0

        return 1.0

    def _confidence(self, sql: str, rows: List[List[Any]]) -> float:
        score = 0.5
        sql_lower = sql.lower()

        if "count(" in sql_lower:
            score += 0.3

        if "where" in sql_lower:
            score += 0.1

        if rows and rows[0] and rows[0][0] is not None:
            score += 0.1

        return min(score, 1.0)
