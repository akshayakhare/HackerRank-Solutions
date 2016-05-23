import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args)throws IOException {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        String tempFive = "5555555555";
        String five = "";
        String three = "";
        for (int i = 0;i < 10000; i++)
            five = five+tempFive;
        three = five.replace('5','3');
        five.concat("5");
        three.concat("3");
        //System.out.println(five.length());
        //System.out.println(five+three);
        Solution obj = new Solution();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testSize = Integer.parseInt(br.readLine());
        int numberOfDigitsArr [] = new int[testSize];
        for(int i = 0;i < testSize; i++){
            numberOfDigitsArr[i] = Integer.parseInt(br.readLine());
        }
        int count = 0;
        int noOfDig = 0;
        String output = "";
        while(count < testSize){
            noOfDig = numberOfDigitsArr[count];
            if (noOfDig < 3 || noOfDig == 4 ||  noOfDig == 7)
                output = "-1";
            else if(noOfDig % 3 == 0){
                output = five.substring(0,noOfDig);
            } else if(noOfDig % 3 == 1){
                output = five.substring(0,noOfDig-10)+three.substring(0,10);
            }else if(noOfDig % 3 == 2){
                output = five.substring(0,noOfDig-5) + three.substring(0,5);
            } 
            System.out.println(output);
            count ++;
            output = "";
        }
    }
}
