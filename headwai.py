from typing import Union, List, Dict
import asyncio
import websockets
import json


class EvaluationResult:
    """Represents the result of an evaluation."""
    
    def __init__(self, score: float, feedback: str):
        self.score = score
        self.feedback = feedback

    def __repr__(self) -> str:
        return f"EvaluationResult(score={self.score}, feedback={self.feedback!r})"


def parse_evaluation_results(results: List[Dict[str, Union[float, str]]]) -> List[EvaluationResult]:
    """Transforms evaluation results from JSON into a list of EvaluationResult objects."""
    return [EvaluationResult(result['score'], result['feedback']) for result in results]


async def send_evaluation_request(
        uri: str, 
        headers: Dict[str, str], 
        queries: Union[List[str], str], 
        reference_answers: Union[List[str], str], 
        generated_answers: Union[List[str], str],
    ) -> List[EvaluationResult]:
    """Sends a correctness evaluation message to a given URI and returns the evaluation results."""
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        payload = {
            "action": "sendMessage",
            "message": {
                "queries": queries,
                "reference_answers": reference_answers,
                "generated_answers": generated_answers,
            },
        }

        await websocket.send(json.dumps(payload))
        
        response = await websocket.recv()
        try:
            response_json = json.loads(response)
            if "message" in response_json and "correctnessEval" in response_json:
                eval_results = json.loads(response_json["correctnessEval"])
                return parse_evaluation_results(eval_results)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON response: {e}")

        raise RuntimeError("No valid evaluation results received.")


def evaluate_correctness(
        queries: Union[List[str], str], 
        reference_answers: Union[List[str], str], 
        generated_answers: Union[List[str], str],
        api_key: str, 
        websocket_url: str = "wss://example.com/prod/",
    ) -> List[EvaluationResult]:
    """Evaluates the correctness of generated answers against reference answers."""
    headers = {"x-api-key": api_key}
    
    try:
        return asyncio.run(send_evaluation_request(
            websocket_url, headers, queries, reference_answers, generated_answers
        ))
    except Exception as e:
        raise RuntimeError(f"Failed to evaluate correctness: {e}")
