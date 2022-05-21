n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

cnt = 1
def recursivecall(count):
    if count == 0: # 무한 루프 방지
        return
    
    global cnt
    if cnt == n + 1: # 한번이라면
        def recursivecall1(count):
            b = ['"재귀함수가 뭔가요?"','"재귀함수는 자기 자신을 호출하는 함수라네"','라고 답변하였지.']
            for i in b:
                print("____" * n + i)
        return(recursivecall1(count))
    elif cnt != n + 1: # 한번 이상
        def recursivecall2(count):
            c = ['"재귀함수가 뭔가요?"','"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.','마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.','그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
            global cnt
            for i in c:
                print('____' * (cnt-1) + i)
            cnt += 1
            if cnt == n + 1: # 한번 더 return
                return recursivecall(count)
            else:
                return recursivecall2(count)
        return(recursivecall2(count))
    
    count -= 1
    recursivecall(count)

def recursivecallast(count):
    print("____" * (count -1) + '라고 답변하였지.')
    if count == 1:
        return '라고 답변하였지.'
    else:
        count -= 1
        return recursivecallast(count)

recursivecall(n)
recursivecallast(n)
