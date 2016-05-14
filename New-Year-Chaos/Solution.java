import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException{
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        String queueSize[] = new String [size];
        String queueContent[] = new String[size];
        for(int i = 0;i < size; i++){
            queueSize[i] = br.readLine();
            queueContent[i] = br.readLine();
        }
        int count = 0;
        int queueLength = 0;
        int totalBribes = 0;
        int temp = 0;
        n:
        while(count < size){
            queueLength = Integer.parseInt(queueSize[count]);
            int queue [] = new int[queueLength];
            String queueDivided [] = queueContent[count].split("\\s+");
            for(int i = 0; i < queueLength; i++){
                queue[i] = Integer.parseInt(queueDivided[i]);
            }
            for(int i = 0; i < queueLength; i++){
                if((queue[i] - i) > 3) // Since the index starts from 0, the index is one shorter than the actual value.
                {
                    System.out.println("Too chaotic");
                    break n;
                }
                else if((queue[i] - i) > 1){
                    totalBribes = totalBribes + (queue[i] - i-1);
                }
            }
            System.out.println(totalBribes);
            count ++;
        }
        
    }
}
