
class ErrorResponse():
    @staticmethod
    def get_error_response(error_code: int, error_message: str):
        return {
            "error": {
                "code": error_code,
                "message": error_message
            }
        }
