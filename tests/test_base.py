from evaluators.base_evaluator import BaseEvaluator


class DummyEvaluator(BaseEvaluator):

    def evaluate(self, input_data):
        return "working"


evaluator = DummyEvaluator()

print(evaluator.evaluate({}))