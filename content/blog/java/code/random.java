
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class RandomTest {
    private static int upperBound(List<BigDecimal> data, BigDecimal target) {
        int begin = 0;
        int end = data.size();

        while(begin < end) {
            int mid = (begin + end) / 2;

            if(data.get(mid).compareTo(target)<0) {
                begin = mid + 1;
            }
            else {
                end = mid;
            }
        }
        return end;
    }
    public static void main(String[] args) {
        Random random = new Random();
        String[] itemName = {
                "몬스터소환비서:소환감룡",
                "몬스터소환비서:소환거마왕",
                "몬스터소환비서:소환건룡",
                "몬스터소환비서:소환고구려왕주몽",
                "몬스터소환비서:소환단조",
                "몬스터소환비서:소환마령",
                "몬스터소환비서:소환마사",
                "몬스터소환비서:소환묵룡",
                "몬스터소환비서:소환부여왕대소",
                "몬스터소환비서:소환북천황",
                "몬스터소환비서:소환사령웅",
                "몬스터소환비서:소환스사노오",
                "몬스터소환비서:소환암흑룡",
                "몬스터소환비서:소환이명",
                "몬스터소환비서:소환조사장",
                "몬스터소환비서:소환진룡",
                "몬스터소환비서:소환흑룡",
                "몬스터소환비서:소환궁기",
                "몬스터소환비서:소환대장군",
                "몬스터소환비서:소환도올",
                "몬스터소환비서:소환도철",
                "몬스터소환비서:소환산신대왕",
                "몬스터소환비서:소환수호백호",
                "몬스터소환비서:소환수호주작",
                "몬스터소환비서:소환수호청룡",
                "몬스터소환비서:소환수호현무",
                "몬스터소환비서:소환수호황룡",
                "몬스터소환비서:소환아랑",
                "몬스터소환비서:소환암흑구미호",
                "몬스터소환비서:소환유성지",
                "몬스터소환비서:소환적혈광마",
                "몬스터소환비서:소환천제벽옥",
                "몬스터소환비서:소환청의태자비",
                "몬스터소환비서:소환파괴왕",
                "몬스터소환비서:소환푸른빛용",
                "몬스터소환비서:소환해골왕",
                "몬스터소환비서:소환혈마화",
                "몬스터소환비서:소환혼돈",
                "몬스터소환비서:소환흑치명",
                "몬스터소환비서:탐험해적선장"
        };
        BigDecimal arr [] = {
                new BigDecimal("0.290782204"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.116312882"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.436173306"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.290782204"),
                new BigDecimal("0.581564408"),
                new BigDecimal("1.744693225"),
                new BigDecimal("0.581564408"),
                new BigDecimal("0.581564408"),
                new BigDecimal("2.907822041"),
                new BigDecimal("6.978772899"),
                new BigDecimal("6.978772899"),
                new BigDecimal("6.978772899"),
                new BigDecimal("6.978772899"),
                new BigDecimal("2.907822041"),
                new BigDecimal("0.581564408"),
                new BigDecimal("11.631288165"),
                new BigDecimal("0.581564408"),
                new BigDecimal("0.581564408"),
                new BigDecimal("0.581564408"),
                new BigDecimal("11.631288165"),
                new BigDecimal("1.744693225"),
                new BigDecimal("11.631288165"),
                new BigDecimal("1.744693225"),
                new BigDecimal("0.581564408"),
                new BigDecimal("0.581564408"),
                new BigDecimal("0.581564408"),
                new BigDecimal("14.539110206")
        };
        List<BigDecimal> sumList = new ArrayList<>();
        BigDecimal sum = new BigDecimal("0");
        for(BigDecimal cur : arr){
            sum = cur.add(sum);
            sumList.add(sum);
            System.out.println(sum);
        }
        for(int i=0;i<100;i++){
            BigDecimal ran = new BigDecimal(String.valueOf(random.nextDouble()*100));
            int index = upperBound(sumList,ran);
            if(index <= 8)
                System.out.println(ran + "\t\t" +sumList.get(index) + "\t\t"+index+"번째 \t\t"+itemName[index]+"\t\t"+ arr[index]);
        }
    }
}