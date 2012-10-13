Pig-Min Rescue Tool
======================
호스팅 문제로 [Pig-Min](http://pig-min.com)의 데이터베이스가 갑자기 롤백되어 글을 복구하기 위해 만든 툴입니다.

HanRSS의 JSON 데이터를 텍스트큐브에 맞는 SQL문으로 바꿔주는 기능을 합니다.

HanRSS JSON 데이터는 이 주소에서 얻을 수 있습니다:

http://www.hanrss.com/myfeeds_main_items.qst?fsrl=*&ssrl=*&ts=*&offset=0&expand=1

*는 소스보기 기능을 사용해 적당히 찾아야 합니다.

한번에 25개까지 긁을 수 있으니 다음 페이지 글 데이터를 받아오려면 offset을 25, 50, 75...로 설정하면 됩니다.

...한RSS에서 글 살리고 싶은분은 잘 수정해서 써보세요.