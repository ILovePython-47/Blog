import streamlit as st

st.title("Airplanes type around the world")
st.write("This is a simple app to show the airplanes type around the world")

option1 = st.selectbox(
  "Select country:",
  ("Germany", "France", "USA", "UK", "Italy", "Spain", "Japan", "China", "Russia")
)

def showgermany():
  if option2 == 'Boeing 777':
    st.video('https://www.youtube.com/watch?v=JFKvSGoCJwE&pp=ygUKYm9laW5nIDc3Nw%3D%3D')
    st.write(
      '''The Boeing 777, commonly known as triple seven, is a long-range widebody aircraft developed by Boeing. It is the largest twinjet ever manufactured. The aircraft was introduced to fill the gap between Boeing 767 and 747 and replace older DC-10s and L-1011 tri-jets. Launched on October 14, 1990, United Airlines became the launch customer.

The prototype rolled out on April 9, 1994, and the aircraft completed its maiden flight on June 12, the same year. In a typical 3 class configuration, the aircraft could accommodate up to 368 passengers. The type could fly from 9,700 to 15,843 km. On June 7, 1995, the B777-200 started to fly with United.

In the late 1980s, DC-10 and L-1011 were getting old and were to be retired soon. Airbus was working on A330 and A340, whereas McDonnell Douglas was working on the MD-11. Boeing considered stretching the 767 named 767-X. But airlines weren't interested in it. So, Boeing went for a clean sheet design. Airlines were interested in the broader fuselage cross-section, fully flexible interior configurations, and short- to intercontinental-range capability. This resulted in the development of the Boeing 777, which opted for the twin-engine configuration.'''
    )
  if option2 == 'Boeing 727':
    st.video("https://www.youtube.com/watch?v=5y7RytjGeF4&pp=ygUKYm9laW5nIDcyNw%3D%3D")
    st.write(
      '''The Boeing 727 is a narrow-body aircraft developed by Boeing in the early 1960s. After the development of 707, there was a need for smaller jets that could serve small airports. So the 727 was launched. The program had received orders for 40 aircraft each from United and Eastern Airlines at its launch. The plane took to the skies for the first time on February 9, 1963. One year later, the type entered service with Eastern Airlines on February 1, 1964. The plane was produced for more than two decades, and the last one rolled out in September 1984. Boeing built 1,832 727 tri-jets.

Boeing 727 is the only trijet produced by Boeing. It is powered by  Pratt & Whitney JT8D low-bypass turbofans and has a T-tail. All three engines are located at the back of the aircraft. The airline could carry around 106 passengers in two classes over 4,170 km.'''
    )

  if option2 == 'CRJ Series':
    st.video("https://www.youtube.com/watch?v=MmQ-yPzb0Lg&pp=ygUKQ1JKIFNlcmllcw%3D%3D")
    st.write(
      '''CRJ series(Canadair Regional Jet) is a regional jet series developed by Bombardier Aerospace. Launched with Lufthansa CityLine, the aircraft completed its maiden flight on May 10, 1991. The first generation (CRJ 100/200) was launched in 1991, and the second generation (CRJ700 series) was launched in 1999. 

After the success of the challenger series, Canadair launched the CRJ project with a primary goal to enter the market in the early 1990s and sell around 400 planes. The process was economical, and development costs were less than other turboprop projects. Keeping in mind the success and customer request, CRJ 200 was manufactured. Some minor changes were made, new engines were added, and the plane was more advanced.

The CRJ 200 completed its maiden flight in 1991. After the success of the CRJ 200 aircraft, the stretched CRJ 700 was launched. The series was further extended to CRJ 900, which could accommodate more passengers. The airliner faced major competition from Embraer aircraft. E-Jet family was also taking over the market, so CRJ 1000 was launched to compete with the type. Despite all these innovations, the aircraft couldn't keep up with the new aircraft from Embraer and other manufacturers.'''
    )

  if option2 == 'Airbus A320 Family':
    st.video('https://www.youtube.com/watch?v=UWb-3ACl-mU&pp=ygULQWlyYnVzIEEzMjA%3D')
    st.write(
      '''Launched in March 1984, the A320 family is a narrow-body family of jets developed by Airbus. The prototype flew three years later, on February 22, 1987. On April 18, 1988, Airbus delivered its first A320 to Air France. 10,176 A320 family aircraft have been delivered as of December 2021.

Some major A320 family aircraft operators are Indigo, American Airlines, China Eastern Airlines, EasyJet, China Southern Airlines, etc. Like the 737 families, the A320 family also has many members in its family, which consist of Airbus A318, Airbus A319, Airbus A320, Airbus A321, and more advanced neo family jets.

After developing A300 and A310, Airbus started to look into the single-aisle narrow-body market, mainly occupied by Boeing 737 and Douglas DC-9. The A320 family received orders for 96 aircraft when it was launched in 1984. Air France was the launch customer ordering 25 jets along with an option for additional 25 more aircraft.

After 1,200 hours of test flight across 530 flights, the airline was awarded European Joint Aviation Authorities (JAA) certification on February 26, 1988. The base variant A320 was stretched more, and the A321 was launched, which is 6.94 meters (22 ft 9 in) longer than the A320. When A320 was shrunk a little, a smaller A319 was born. When further shrunk, the A318 was born. Airbus A318 was built to challenge Boeing 737 Classics but faced challenges from the next generation and MAX series aircraft. Airbus has been delivering more narrow-body jets than Boeing in recent years.'''
    )

  if option2 == 'Boeing 737 Family':
    st.write(
      '''The Boeing 737 is a narrow-body aircraft manufactured by Boeing in Renton Factory, Washington. It is the most produced aircraft in commercial aviation, with 10,877 planes delivered as of December 2021.

Boeing 737 took to the skies for the first time on April 9, 1967, 54 years ago and is very famous for medium-haul flights. Ten months later, on February 10, 1968, the first aircraft was delivered to Lufthansa. The 737 family is still a popular choice for airlines around the globe. It is flown by airlines like Southwest Airlines, Ryanair, United Airlines, and American Airlines.

Boeing wanted to build an aircraft that could offer shorter routes, something smaller than the Boeing 727. Aircraft of similar sizes like Douglas DC-9 and Fokker F28 were already manufactured and getting flight certification. Lufthansa was the launch customer with an order for 21 jets worth roughly around $67 million at that time. The first generation includes 737-100 and 737-200. 

Boeing 737 Classic, which is the second generation, soon followed. They were more advanced than the previous generation with new engines. 737 Next Generation soon followed, which is the third generation, and most of the 737s flown today belong to this group, including the models 737-600/700/800/900 series and the extended range -700ER/900ER variants.'''
    )

  if option2 == 'Douglas DC-3':
    st.write(
      '''The Douglas DC-3 was originally intended as an airliner but after just 607 airliner variants were built, the DC-3 was re-tasked to serve in a military transport roll and the rest of the 16,079 DC-3s built between 1935 and 1952 did just that.

According to Wikipedia, the total production breakdown of DC-3 includes all variants as follow:

607 civilian variants
10,048 military C-47 and C-53 derivatives built at Santa Monica, California, Long Beach, California, and Oklahoma City
4,937 built under license in the Soviet Union (1939–1950) as the Lisunov Li-2 (NATO reporting name: Cab)'''
    )

###################################################################################################

if option1 == 'Germany':
  option2 = st.selectbox(
    "Select type:",
    ("Boeing 777", "Boeing 727", "CRJ Series", "Airbus A320 Family", "Boeing 737 Family", "Douglas DC-3")
  )
  showgermany()
if option1 == 'France':
  option2 = st.selectbox(
    "Select type:",
    ("Concorde", "Boeing 747-100", "CRJ Series", "Airbus A320 Family", "Boeing 737 Family", "Douglas DC-3")
  )
  showgermany()