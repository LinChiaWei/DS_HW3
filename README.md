# DS_HW3

## 策略想法
策略上使用了兩種方法，一個有使用模型預測，另一個則沒有，最後取結果比較好的方法上傳。
1. 使用LSTM預測隔一天的的用電量及產電量，透過預測出來的結果進行策略的構想。
2. 使用過去七天的用電量和產電量，並取用平均值，計算總共需要購買或是賣出的電量，並取平均以每小時進行交易。

## 方法一 : 
### 資料處理
* 先取出要進行訓練的資料，前七天的資料加上一天用來測試的資料且每小時一筆，共有192筆  
  ![image](https://github.com/LinChiaWei/DS_HW3/blob/main/images/generate.png)
  ![image](https://github.com/LinChiaWei/DS_HW3/blob/main/images/cons.png)
* 將資料進行正規化，將值壓在0-1之間，以利於訓練
* 將資料分割成訓練及測試資料，比例為168:24
### 模型訓練
* 模型訓練分成兩個部分，一個為用電量，另一個為產電量
  1. 將資料分成時間序列格式，以144天為基底，生成取24天
  2. 分別生成訓練時要使用的訓練資料，預測資料
  3. 模型部分皆使用了三層LSTM layer，優化器使用adam，loss使用MSE，架構如下: 
      ![image](https://github.com/LinChiaWei/DS_HW3/blob/main/images/LSTM.png)

### 預測結果對比
將模型預測結果與測試資料進行比較
1. 生產電量的預測比較  
