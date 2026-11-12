class Student:
    def __init__(self, student_id, full_name, class_form, gender, dob, scores=None):
        self.student_id = student_id
        self.full_name = full_name
        self.class_form = class_form
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores is not None else {}  # dictionary of subject: score

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_form": self.class_form,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            full_name=data["full_name"],
            class_form=data["class_form"],
            gender=data["gender"],
            dob=data["dob"],
            scores=data.get("scores", {})
        )
