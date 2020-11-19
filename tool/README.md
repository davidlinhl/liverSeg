Useful scripts for preprocess and postprocessing medical image data.


```shell

count=0 ;
total=`ls -l | wc -l`
for f in `ls`;
do count=`expr $count + 1`;
echo $count / $total;
dcm2niix -f $f -o ../nii_raw/ -c $f $f
echo -e "\n"
echo -e "\n"
done



count=0 ;
for f in `ls`;
do count=`expr $count + 1`;
echo $count / `ls -l | wc -l`;
echo ${f};
echo -e "\n";
itksnap -s ../label/${f} -g ${f} --geometry 1920x1080+0+0;
# cp ../label/${f} ../manual-label/
done



count=0 ;
for f in `ls`;
do
# 四个 beep
(sleep 2m; beep;) &
pid2=$!
(sleep 4m; beep; beep;) &
pid4=$!
(sleep 6m; beep; beep; beep;) &
pid6=$!
(sleep 8m; beep; beep; beep; beep; ) &
pid8=$!

# 计数
count=`expr $count + 1`;
echo $count / `ls -l | wc -l`;
echo ${f};
echo -e "\n";

# 打开扫描和标签
itksnap -s ./${f} -g ../nii/${f} --geometry 1920x1080+0+0;

# 文件归档
# cp ./${f} ../manual-label/
mv ./${f} ../manual-finished/

# 关闭没响的beep
kill -9 $pid2
kill -9 $pid4
kill -9 $pid6
kill -9 $pid8
done


```
