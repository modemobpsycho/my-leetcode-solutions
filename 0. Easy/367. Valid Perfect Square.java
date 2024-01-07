class Solution {
    public boolean isPerfectSquare(int num) {
        for(long i=0; i<=num; i++)
        {
            long square = i*i;
            if(square == num) return true;
            else if (square > num) break;
        }
        return false;
    }
}