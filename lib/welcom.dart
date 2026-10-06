import 'package:flutter/material.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:connect_four/main.dart'; // Replace this with your ConnectFourGame import
import 'package:connect_four/main2.dart'; // Replace this with your ConnectFourGame import

class Welcome extends StatelessWidget {
  const Welcome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 226, 224, 224),
      appBar: AppBar(
        title: const Text(
          'Connect Four Game',
          style: TextStyle(
            fontWeight: FontWeight.bold,
            color: Color.fromARGB(255, 95, 18, 109),
          ),
        ),
        backgroundColor: const Color.fromARGB(255, 226, 224, 224),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              width: 250,
              height: 400,
              child: TypewriterAnimatedTextKit(
                text: ['Welcome to Connect Four Game!'],
                textStyle: const TextStyle(
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 95, 18, 109),
                  fontSize: 32,
                ),
                speed: const Duration(milliseconds: 100),
                totalRepeatCount: 1,
                pause: const Duration(milliseconds: 1000),
              ),
            ),
            // const SizedBox(height: 180), // Adjust vertical spacing here
            // const SizedBox(height: 100),
            ElevatedButton(
              onPressed: () {
                // Navigate to the ConnectFourGame screen when the button is pressed
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ConnectFourGame()),
                );
              },
              child: const Text('Player vs Computer'),
            ),
            const SizedBox(height: 20),
            
            
            ElevatedButton(
              onPressed: () {
                // Navigate to the ConnectFourGame screen when the button is pressed
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ConnectFourGame2()),
                );
              },
              child: const Text('Computer vs Computer'),
            ),
         
         
         
          ],
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: Welcome(),
  ));
}
