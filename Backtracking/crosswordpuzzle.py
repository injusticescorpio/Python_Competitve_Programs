def main():
    mat=[
        ['+','+','-','-','-'],
        ['+','-','+','+','+'],
        ['+','-','-','-','+'],
        ['+','-','+','-','+'],
        ['+','+','+','-','+']
    ]
    def check_pos():
        li=[]
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if mat[i][j]=='-':
                    li.append((i,j))
        return li
    def check_horizontal(i,j,word):
        if mat[i][j:j+len(word)]==['-']*len(word):
            return True
        else:
            return False
    def add_word_horizontal(i,j,word):
        mat[i][j:j+len(word)]=[k for k in word]
    def check_vertical(i,j,word):
        if list(list(list(zip(*mat)))[j][i:i + len(word)])==['-']*len(word):
            return True
        else:
            return False

    def add_word_vertical(i,j,word):
        k=0
        for a in range(i,i+len(word)):
            mat[a][j]=word[k]
            k+=1
    def remove_word_vertical(i,j,word):
        for a in range(i,i+len(word)):
            mat[a][j]='-'
    def remove_word_horizontal(i,j,word):
        mat[i][j:j + len(word)] = [i for i in '-'*len(word)]
    li=check_pos()
    print(f"li=={li}")
    # print(f"mat=={mat}")
    val=['act','rat','cot','top']
    def dfs(x,val):
        for i in range(0, len(mat)):
            print(' '.join(mat[i]))
        print(f"val=={val}")
        if x>=len(val) or len(val)==0:
            return
        value = val.pop(0)
        for i in range(0, len(mat)):
                for j in range(0, len(mat)):
                    if (mat[i][j]=='-' or mat[i][j]==value[0]) and check_horizontal(i,j,value):
                        add_word_horizontal(i,j,value)
                        dfs(x+1,val)
                        val.append(value)
                        remove_word_horizontal(i,j,value)
                        li.append((i,j))
                    elif (mat[i][j]=='-' or mat[i][j]==value[0]) and check_vertical(i,j,value):
                        add_word_vertical(i,j,value)
                        dfs(x+1,val)
                        val.append(value)
                        remove_word_vertical(i,j,value)
                        li.append((i,j))
    dfs(0,val)
    for i in range(0,len(mat)):
        print(' '.join(mat[i]))











main()

