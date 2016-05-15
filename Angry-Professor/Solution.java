import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException{
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testSize = Integer.parseInt(br.readLine());
        String queueSize[] = new String [testSize];
        String queueContent[] = new String[testSize];
        for(int i = 0;i < testSize; i++){
            queueSize[i] = br.readLine();
            queueContent[i] = br.readLine();
        }
        int count = 0;
        String strStudLimits []= new String[2];
        int totalBribes = 0;
        int tempCount = 0;
        n:
        while(count < testSize){
            strStudLimits = queueSize[count].split("\\s+");
            int studLimits[] = new int[2];
            for(int i = 0; i < 2 ; i++){
                studLimits[i] = Integer.parseInt(strStudLimits[i]);
            }
            int studTime [] = new int[studLimits[0]];
            String queueDivided [] = queueContent[count].split("\\s+");
            for(int i = 0; i < studLimits[0]; i++){
                studTime[i] = Integer.parseInt(queueDivided[i]);
            }
            tempCount = 0;
            for(int i = 0; i < studTime.length; i++){
                if(studTime[i] <= 0)
                    tempCount ++;
            }
            if(tempCount >= studLimits[1]){
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
            count ++;
        }
        
    }
}
