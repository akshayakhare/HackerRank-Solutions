import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args)throws IOException {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Solution obj = new Solution();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testSize = Integer.parseInt(br.readLine());
        int numberOfDigitsArr [] = new int[testSize];
        for(int i = 0;i < testSize; i++){
            numberOfDigitsArr[i] = Integer.parseInt(br.readLine());
        }
        System.out.println(obj.addNumbers(2,"6","6"));
        int count = 0;
        int noOfDig = 0;
        String output = "";
        while(count < testSize){
            noOfDig = numberOfDigitsArr[count];
            if (noOfDig < 3)
                output = "-1";
            else if(noOfDig % 3 == 0){
                output = obj.addNumbers(noOfDig,"5","");
            } else if(noOfDig == 5){
                output = obj.addNumbers(noOfDig,"3","");
            } else{
                int temp = noOfDig;
                temp = temp - 5;
                if(temp > 0 && temp % 3 == 0){
                    output = obj.addNumbers(temp,"5","").concat(obj.addNumbers(5,"3",""));
                } else{
                    temp = noOfDig - 1;
                    if(temp % 3 == 0){
                        output = obj.addNumbers(temp,"5","");
                    } else {
                        output = obj.addNumbers(temp-1,"5","");
                    }
                }
                //output = "-2";
            }
            System.out.println(output);
            count ++;
            output = "";
        }
    }
    
    /*public String addNumbers(int size, String num){
        String returnValue = "";
        int count = 1;
        returnValue = num;
        while(count < size){
            if(count*2 <= size){
                returnValue = returnValue.concat(returnValue);
                count = count *2;
            }
            else {
                returnValue = returnValue.concat(num);
                count ++;
            }
        }
        return returnValue;
    }*/
    public String addNumbers(int size, String num,String returnValue){
        if(size <= 0){
            return returnValue;
        } else if(returnValue.length()*2 <= size){
            int len = returnValue.length();
            returnValue = returnValue.concat(returnValue);
            return addNumbers(size-len,num,returnValue);
        } else {
            returnValue = returnValue.concat(num);
            return returnValue.concat(addNumbers(size-returnValue.length(),num,num));
        }
        //return returnValue;
    }
}
