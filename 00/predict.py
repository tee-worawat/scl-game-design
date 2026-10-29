"""Read and predict BEFORE running. This tiny example is not the mission solution.
อ่านและคาดการณ์ก่อนรัน ตัวอย่างเล็กนี้ไม่ใช่เฉลยภารกิจ
"""
def add_points(score, bonus):
    return score + bonus

class Badge:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def collect(self, bonus):
        self.points = add_points(self.points, bonus)

nova = Badge('Nova')
pip = Badge('Pip')
nova.collect(2)
print(nova.points, pip.points)
print(add_points(4, 3))
print(nova.points)
