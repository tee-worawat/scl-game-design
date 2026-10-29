"""Learner feedback for functions and independent objects; no solution code."""
import starter as work

def function_check():
    assert work.energy_after_move(3, 1) == 2, '3 energy minus cost 1 should return 2'
    assert work.energy_after_move(0, 1) == 0, 'Unaffordable move must keep energy at 0'
    assert work.energy_after_move(3, 0) == 3, 'Zero cost keeps energy unchanged'
    try:
        work.energy_after_move(3, -1)
    except ValueError:
        return
    raise AssertionError('Negative cost must raise ValueError')

def object_check():
    a, b = work.Robot('A', 1), work.Robot('B', 3)
    assert (a.name, a.energy, a.position) == ('A', 1, 0), 'Check instance attributes'
    assert a.move() is True, 'Affordable move returns True'
    assert (a.energy, a.position) == (0, 1), 'Move spends 1 energy and advances 1'
    assert a.move() is False, 'Empty robot must return False'
    assert (a.energy, a.position) == (0, 1), 'Failed move must not change state'
    assert (b.energy, b.position) == (3, 0), 'Moving A must not change B'
    a.recharge()
    assert a.energy == 2, 'Recharge adds 2'
    a.recharge(); a.recharge()
    assert a.energy == 5, 'Recharge caps at 5'
    assert b.energy == 3, 'Recharge must affect only its receiver'

if __name__ == '__main__':
    for label, check in [('Function / ฟังก์ชัน', function_check), ('Objects / ออบเจ็กต์', object_check)]:
        try:
            check()
        except (AssertionError, NotImplementedError, AttributeError, TypeError) as error:
            print('NEXT / ฝึกต่อ:', label, '-', error)
        else:
            print('PASS / ผ่าน:', label)
    print('Then manually test play(): win, loss, invalid command, quit and a fresh restart.')
    print('จากนั้นทดสอบ play(): ชนะ แพ้ คำสั่งผิด ออก และเริ่มใหม่')
