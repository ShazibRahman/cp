class practice
{
	public static void main(String[] args) 

	{   int [] heights={1,8,6,2,5,4,8,3,7};
		System.out.println(max_r( heights) );
		
	}
	public static int max_r(int [] heights)
	{    
		int left=0,right=heights.length-1, max_=0,k=0;
		while (left < right)
		{
			 k=Math.min(heights[left], heights[right])*(right-left);
		
			 if (k> max_)
			 {
			 	max_=k;
			 }
			 if (heights[left]> heights[right])
			 {
			 	right-=1;
			 }
			 else
			 {
			 	left+=1;
			 }
        

	}
	return max_;
}
}