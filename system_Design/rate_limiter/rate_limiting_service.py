from datetime import datetime
import time

class TokenBucketAlgorithm:
    bucket = []
    bucket_size = 3
    refill_rate = (1, 5) # (token_count,time_frame_seconds)
    HTTP_429_STATUS = 429
    time_data = "25/05/99 02:35:5.523"
    format_data = "%d/%m/%y %H:%M:%S.%f"
    last_refill_at = datetime.strptime(time_data, format_data)

    def is_refill_bucket(self):
        return True if len(self.bucket) < self.bucket_size else False

    def time_to_fill(self):
        t = self.last_refill_at - datetime.now()
        return True if t.seconds >= self.refill_rate[1] else False

    def refill_token(self):
        if self.is_refill_bucket() and self.time_to_fill():
            self.bucket.append(int(time.time()))
            self.last_refill_at = datetime.now()
            return 301
        return 429

    def get_token(self):
        token = None
        try:
            token = self.bucket.pop()
            self.refill_token()
        except IndexError:
            return token

    def pass_through(self, req):
        token = self.get_token()
        if not token:
            return self.HTTP_429_STATUS
        response = request.g




