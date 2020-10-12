#include <bits/stdc++.h>
# define my_sizeof(type) ((char *)(&type+1)-(char*)(&type)) 


int max_r(int h[])
{
	int left=0,right=8;
	int max_=0,k=0;
	while (left < right)
	{
		k=std::min(h[left], h[right])*(right-left);
		if (k>max_)
		{
			max_=k;
		}
		if (h[left]>h[right])
		{
			right--;

		}
		else
		{
            left++;
		}

	}
    return max_;
}

int main()
{
	int h[]={1,8,6,2,5,4,8,3,7};
	std::cout<<max_r(h);

}