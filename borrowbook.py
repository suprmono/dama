import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class BookManag:

    books = []
    menus = []
    borr_list = []

    def __init__(self):
        print ('----初始化书库-----')
        self.books = ['三国演义','红楼梦','西游记','水浒传']
        self.menus = ['借书','还书','添加书','退出']

    def show_menu(self):
        print('------------欢迎使用图书管理系统------------')
        for i in range(0, len(self.menus)):
            print (i,self.menus[i])
        print('------------------------------------------') 

    def show_books(self):
        print ('书库中还有以下书籍：', '')
        print('------------------------------------------')
        for i in range(0, len(self.books)):
            print (i+1,self.books[i])
        print('------------------------------------------')    
        
    def add_book(self,add_type):
        book_name = input('请输入书籍的名称:')
        msg = '还书'
        if add_type == 1:
            msg = '添加'
        else:
            if book_name not in self.borr_list:
                print('书籍【'+ book_name +'】不存在，还书失败！-------------')
            else:
                self.books.insert(0,book_name)
                print('书籍【'+ book_name +'】'+ msg +'成功-------------')

    def remove_book(self,book_index):
        book_name = self.books[book_index - 1]
        if book_name.strip()!='':
           self.books.pop(book_index-1)


    def chooice_book(self):
        n = int(input('请选择要借阅书籍的编号:'))
        print('------------------------------------------')
        if n>=1 and n<=len(self.books):
            print('成功借阅书籍：【'+ self.books[n-1]+'】')
            self.borr_list.insert(0,self.books[n-1])
            self.remove_book(n)
            print('------------------------------------------')
        else:
            print('借阅失败，书籍不存在！')

    def borrow_book(self):
        self.show_books()
        self.chooice_book()                


if __name__ == "__main__":
        bm = BookManag()
        exit_flag= 0
        while(exit_flag == 0):
            bm.show_menu()
            n = int(input('请选择菜单:'))
            if n<0 or n>3:
                print('-------输入有误，请重新输入------')
            if n==0:
                bm.borrow_book()
            if n==1:
                bm.add_book(0)
            if n==2:
                bm.add_book(1)
            if n==3:
                exit_flag = 1
                print('-------谢谢使用图书管理系统，再见！------')
    

