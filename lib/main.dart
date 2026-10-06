// import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class ConnectFourGame extends StatefulWidget {
  @override
  _ConnectFourGameState createState() => _ConnectFourGameState();
}

class _ConnectFourGameState extends State<ConnectFourGame> {
  List<List<int>> board = [[]]; // Initialize board
  // late AudioCache audioCache; // Initialize AudioCache
  // AudioPlayer? audioPlayer; 
  // Function to fetch board data from the Flask API
Future<void> fetchBoard() async {
  try {
    final response = await http.get(Uri.parse('http://172.20.10.3:5000/get_board'));
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      setState(() {
        board = List<List<int>>.from(data['board'].map((row) => List<int>.from(row.map((cell) => cell.toInt()))));
        print(board);
      });
        checkGameOver(); // Check game-over status after updating the board
    } else {
      throw Exception('Failed to load board');
    }
  } catch (e) {
    print('Exception while fetching board: $e');
  }
}

Future<void> makeMoveAndUpdateBoard(int column, int piece) async {
  try {
    final response = await http.post(
      Uri.parse('http://172.20.10.3:5000/make_move'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, int>{'column': column, 'piece': piece}),
    );

    if (response.statusCode == 200) {
      print('Move made successfully');
      await fetchBoard(); // Fetch the updated board after making the move
    } else {
      throw Exception('Failed to make a move');
    }
  } catch (e) {
    print('Exception while making move: $e');
  }
}

Future<void> checkGameOver() async {
  try {
    final response = await http.get(Uri.parse('http://172.20.10.3:5000/game_over'));
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      print('Game Over: ${data['game_over']}');
      if (data['game_over']) {
        showGameOverDialog(context);
      } else {
        print('Game is not over yet.');
      }
    } else {
      print('Failed to check game over: ${response.statusCode}');
    }
  } catch (e) {
    print('Exception while checking game over: $e');
  }
}
Future<void> restartGame() async {
  final url = Uri.parse('http://172.20.10.3:5000/restart'); // Replace with your actual backend URL

  try {
    final response = await http.get(url);
    if (response.statusCode == 200) {
      print('Board reset successfully');
      // Fetch the board data after restarting
      fetchBoard();
    } else {
      print('Failed to reset the board');
    }
  } catch (e) {
    print('Error occurred: $e');
  }
}


void showGameOverDialog(BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text('Game Over'),
        content: Text('The game is over!'), // Customize the content as needed
        actions: [
          TextButton(
            onPressed: () {
              // Reset the game or navigate back to the main screen
              Navigator.pop(context);
              restartGame(); // Call your restart function if needed
            },
            child: Text('OK'),
          ),
        ],
      );
    },
  );
}

  // Future<void> playTicSound() async {
  //   // Initialize the audioplayers instance
  //   AudioCache player = AudioCache(prefix: 'audio/');
  //   // Play the tic sound
  //   await player.play('tic_sound.mp3');
  // }


  @override
  void initState() {
    super.initState();
    fetchBoard(); 
    // audioCache = AudioCache(prefix: 'audio/'); // Initialize AudioCache
    // audioCache.load('tic.wav'); // Preload the audio file
    fetchBoard();// Fetch board data when the widget is initialized
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 226, 224, 224),
      appBar: AppBar(
        title: const Text('Connect Four Game',style: TextStyle(fontWeight: FontWeight.bold,color:Color.fromARGB(255, 95, 18, 109) ),),
        backgroundColor:const Color.fromARGB(255, 226, 224, 224), 
      ),
      body: Center(
        child:Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            
           
          
           Container(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(15),
              color: Color.fromARGB(255, 58, 96, 248)
            ),
            
            child:  Column(children: [
              const SizedBox(height: 15,),


 GridView.builder(
  shrinkWrap: true,
  gridDelegate: board.isNotEmpty && board[0].isNotEmpty
      ? SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: board[0].length,
          crossAxisSpacing: 4.0,
          mainAxisSpacing: 4.0,
        )
      : SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 1, // Fallback to 1 if board size is invalid
        ),
  itemCount: board.length * (board.isNotEmpty ? board[0].length : 1),
  itemBuilder: (context, index) {
    if (board.isEmpty || board[0].isEmpty) {
      return Center(
        child: Text('Invalid board size'),
      );
    }
    int row = index ~/ board[0].length;
    int col = index % board[0].length;
    return GestureDetector(
      onTap: () async {
        print("the column tapped: $col");
        // await audioCache.play()
        makeMoveAndUpdateBoard(col, 2);

      },
      child: Container(
        width: 40,
        height: 40,
        decoration: BoxDecoration(
          borderRadius: const BorderRadius.all(Radius.circular(50)),
          color: board[row][col] == 0
              ? Color.fromARGB(255, 179, 193, 255)
              : board[row][col] == 1
                  ? Colors.yellow
                  : Colors.red,
        ),
      ),
    );
  },
),


              const SizedBox(height: 15,),
            ],)
           ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                restartGame();
              },
              child: const Text('Reset'),
            ),
          ],
        ),
        )
        
        
        

      );
    
  }
}


