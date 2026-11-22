import enum


class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class Diet(str, enum.Enum):
    veg = "veg"
    egg = "egg"
    non_veg = "non_veg"


class Mode(str, enum.Enum):
    hosting = "hosting"
    looking = "looking"


class OccupationCategory(str, enum.Enum):
    student = "student"
    working_professional = "working_professional"
    self_employed = "self_employed"
    other = "other"