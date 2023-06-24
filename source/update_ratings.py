import models
import math
from sqlalchemy import text
from sqlalchemy.orm import Session

class UpdateRatings:
    def __init__(self, data_ratings):
        self.data_ratings = data_ratings

    def update_ratings(self):
        print(self.data_ratings['data']['ar'])
        print(self.data_ratings['data']['tr'])

        pass