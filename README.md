# Phase-diagram-generation-using-an-equation-of-state
利用Van der Waals equation of state，結合Maxwell construction，建立liquid-gas phase diagrem

#程式功能技術原理
利用Van Der Waals Equation of State為基礎，模擬1mol真實氣體在不同溫度與體積下的壓力行為，並藉由redueced variables，繪製 P–V isotherms(reduced form)。透過 Maxwell construction修正實際P-V isotherm 中非物理震盪區段以求得氣液共存的壓力，進一步建立 T-P phase diagram。使用者可清楚觀察氣體在不同溫度下的體積與壓力變化，理解氣液不穩定區，並透過氣液共存壓力隨溫度變化的趨勢與臨界點，理解不同氣體的相行為。
#Van Der Waals Equation of State:(P+a(n/V)^2)(V-nb)=nRT。
#Maxwell construction:以一條水平線修正Van der Waals isotherm在低於臨界溫度時出現的震盪，使線在P-V isotherm包圍的上下面積相等，以符合氣液兩相在相平衡是具有相同壓力的條件。(∫ from V_l to V_g [P(V, T)-P_eq] dV = 0；P_eq:氣液共存之壓力；P_l:液相壓力；P_g:氣相壓力)
#reduced variables:將實際溫度與體積轉換成相對於臨界點的比例，於此將更好辨識不同溫度下的P-V isotherm。
#臨界溫度:(8*a)/(27*Rb)；臨界體積:3*b；臨界壓力:a/(27*b^2)

#使用方式
使用者input氣體的Van Der Waals 參數a、b 即可，後續會利用這些參數計算對應isotherms，再輸出結果(詳見「程式功能」)。

#程式架構
1.利用a、b，以及氣體常數R，計算臨界溫度、壓力、體積(氣液共存線的終點)
2.利用Van Der Waals Equation計算給定T、V下的P
3利用2.所得之P，繪製P-V isotherms
4.對P-V isotherm的氣液不穩定區進行Maxwell construction，進而求出兩相共存壓力等
5.彙整不同溫度的共存壓力，繪製P-T phase diagram。

#開發過程
1.選定主題卻不知道從何做起:向ChatGpt求助，得到一個大致方向
2.T-P isotherm 輸出結果跟預期不符(輸出:一直線，預期:斜率逐漸變大的曲線):調整V_l、V_g根搜尋範圍；遇到無解或nan時跳過該溫度，避免影響結果
3.起初對Maxwell construction概念的不熟悉:看過幾次參考資料所提及的概念，整理後再向ChatGpt確認自己的理解是否正確，方引用Maxwell construction這個概念

#參考資料來源
1.Atkins & de Paula, Physical Chemistry--Real Gases and Phase Transitions；Wikipedia(Maxwell construction)
2.ChatGpt:確認project方向以及code細部修改、調整
3.Chemical Principles by S. S. Zumdahl and D. J. DeCoste, 8th ed.; 2017(Van Der Waals equation of state)

#程式修改或增強的內容
1.原先P-V isotherm是直接用實際的數值繪製(同時也是ChatGpt給定的方向)，但震盪區實在難以辨識:改用reduced variables使isotherm主要呈現在震盪區，較好觀察
2.進行Maxwell construction時，用Simpson積分，T在鄰近臨界溫度時或V_l、V_g接近時(積分區間過小)，計算頻頻出錯，連帶影響後續計算結果:引入過往沒學過的「quad」提升穩定性及準確性

