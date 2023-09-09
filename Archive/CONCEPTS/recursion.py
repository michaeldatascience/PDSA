'''
Format
int log(int b, int n ) {
    if <<enter base case>> {
        return 1;
    } else {
        return <<enter action case>> ;
    }
}
'''
def rLog(a,b):
    # number=a, base = base
    if (a>b):
        return 1
    
    return(1 + rLog())
