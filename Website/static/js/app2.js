var quiz = {
  JS: [
    {
      id: 1,
      question: "A process can be __________",
      options: [
        {
          a: "single threaded",
          b: "multithreaded",
          c: "both",
          d: "none",
        },
      ],
      answer: "both",
      score: 0,
      status: "",
    },
    {
      id: 2,
      question: "Which of the following is not shared by threads?",
      options: [
        {
          a: "program counter",
          b: "stack",
          c: "program counter and stack",
        },
      ],
      answer: "program counter and stack",
      score: 0,
      status: "",
    },
    {
      id: 3,
      question: "A thread is also called __________",
      options: [
        {
          a: "Light Weight Process",
          b: "Heavy weight Process",
          c: "Process",
        },
      ],
      answer: "Light Weight Process",
      score: 0,
      status: "",
    },
    {
      id: 4,
      question: "A Heavyweight process has _________",
      options: [
        {
          a: "multiple threads of execution",
          b: "single thread of execution",
        },
      ],
      answer: "single thread of execution",
      score: 0,
      status: "",
    },
    {
      id: 5,
      question:
        " The model in which one kernel thread is mapped to many user-level threads is called ___________",
      options: [
        {
          a: "One to Many model",
          b: "Many to Many model",
          c: "Many to One model",
          d: "One to One model",
        },
      ],
      answer: "Many to One model",
      score: 0,
      status: "",
    },
    {
      id: 6,
      question:
        " The model in which one user-level thread is mapped to many kernel level threads is called ___________",
      options: [
        {
          a: "One to Many model",
          b: "Many to One model",
          c: "One to One model",
        },
      ],
      answer: "One to Many model",
      score: 0,
      status: "",
    },
    {
      id: 7,
      question:
        "In the Many to One model, if a thread makes a blocking system call ___________",
      options: [
        {
          a: "a part of the process will be blocked",
          b: "the entire process will run",
          c: "the entire process will be blocked",
        },
      ],
      answer: "the entire process will be blocked",
      score: 0,
      status: "",
    },
    // {
    //   id: 8,
    //   question: "How to write an IF statement in JavaScript?",
    //   options: [
    //     {
    //       a: "if i = 5 then",
    //       b: "if i == 5 then",
    //       c: "if (i == 5)",
    //       d: " if i = 5",
    //     },
    //   ],
    //   answer: "if (i == 5)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 9,
    //   question: "Which of the following is a disadvantage of using JavaScript?",
    //   options: [
    //     {
    //       a: "Client-side JavaScript does not allow the reading or writing of files.",
    //       b: "JavaScript can not be used for Networking applications because there is no such support available.",
    //       c: "JavaScript doesn't have any multithreading or multiprocess capabilities.",
    //       d: "All of the above.",
    //     },
    //   ],
    //   answer: "All of the above.",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 10,
    //   question:
    //     "How to write an IF statement for executing some code if &quot;i&quot; is NOT equal to 5?",
    //   options: [
    //     {
    //       a: "if (i <> 5)",
    //       b: "if i <> 5",
    //       c: "if (i != 5)",
    //       d: "if i =! 5 then",
    //     },
    //   ],
    //   answer: "if (i != 5)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 11,
    //   question: "How does a WHILE loop start?",
    //   options: [
    //     {
    //       a: "while i = 1 to 10",
    //       b: "while (i &lt;= 10; i++)",
    //       c: "while (i &lt;= 10)",
    //     },
    //   ],
    //   answer: "while (i &lt;= 10)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 12,
    //   question: "How does a FOR loop start?",
    //   options: [
    //     {
    //       a: "for (i = 0; i &lt;= 5)",
    //       b: "for (i = 0; i &lt;= 5; i++)",
    //       c: "for i = 1 to 5",
    //       d: "for (i &lt;= 5; i++)",
    //     },
    //   ],
    //   answer: "for (i = 0; i &lt;= 5; i++)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 13,
    //   question: "How can you add a comment in a JavaScript?",
    //   options: [
    //     {
    //       a: "//This is a comment",
    //       b: "&sbquo;This is a comment",
    //       c: "&lt;!--This is a comment--",
    //     },
    //   ],
    //   answer: "//This is a comment",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 14,
    //   question: "How to insert a comment that has more than one line?",
    //   options: [
    //     {
    //       a: "/*This comment has more than one line*/",
    //       b: "//This comment has more than one line//",
    //       c: "&lt;!--This comment has more than one line--&gt;",
    //     },
    //   ],
    //   answer: "/*This comment has more than one line*/",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 15,
    //   question: "What is the correct way to write a JavaScript array?",
    //   options: [
    //     {
    //       a: "var colors = (1:&quot;red&quot;, 2:&quot;green&quot;, 3:&quot;blue&quot;)",
    //       b: "var colors = [&quot;red&quot;, &quot;green&quot;, &quot;blue&quot;]",
    //       c: "var colors = 1 = (&quot;red&quot;), 2 = (&quot;green&quot;), 3 = (&quot;blue&quot;)",
    //       d: "var colors = &quot;red&quot;, &quot;green&quot;, &quot;blue&quot;",
    //     },
    //   ],
    //   answer:
    //     "var colors = [&quot;red&quot;, &quot;green&quot;, &quot;blue&quot;]",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 16,
    //   question: "How do you round the number 7.25, to the nearest integer?",
    //   options: [
    //     {
    //       a: "rnd(7.25)",
    //       b: "Math.round(7.25)",
    //       c: "Math.rnd(7.25)",
    //       d: "round(7.25)",
    //     },
    //   ],
    //   answer: "Math.round(7.25)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 17,
    //   question: "How do you find the number with the highest value of x and y?",
    //   options: [
    //     {
    //       a: "Math.max(x, y)",
    //       b: "Math.ceil(x, y)",
    //       c: "top(x, y)",
    //       d: "ceil(x, y)",
    //     },
    //   ],
    //   answer: "Math.max(x, y)",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 18,
    //   question:
    //     "What is the correct JavaScript syntax for opening a new window called &quot;w2&quot;?",
    //   options: [
    //     {
    //       a: "w2 = window.new(&quot;http://www.w3schools.com&quot;);",
    //       b: "w2 = window.open(&quot;http://www.w3schools.com&quot;);",
    //     },
    //   ],
    //   answer: "w2 = window.open(&quot;http://www.w3schools.com&quot;);",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 19,
    //   question: "JavaScript is the same as Java.",
    //   options: [
    //     {
    //       a: "true",
    //       b: "false",
    //     },
    //   ],
    //   answer: "false",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 20,
    //   question: "How can you detect the client&rsquo;s browser name?",
    //   options: [
    //     {
    //       a: "navigator.appName",
    //       b: "browser.name",
    //       c: "client.navName",
    //     },
    //   ],
    //   answer: "navigator.appName",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 21,
    //   question: "Which event occurs when the user clicks on an HTML element?",
    //   options: [
    //     {
    //       a: "onchange",
    //       b: "onclick",
    //       c: "onmouseclick",
    //       d: "onmouseover",
    //     },
    //   ],
    //   answer: "onclick",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 22,
    //   question: "How do you declare a JavaScript variable?",
    //   options: [
    //     {
    //       a: "var carName;",
    //       b: "variable carName;",
    //       c: "v carName;",
    //     },
    //   ],
    //   answer: "var carName;",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 23,
    //   question: "Which operator is used to assign a value to a variable?",
    //   options: [
    //     {
    //       a: "*",
    //       b: "-",
    //       c: "=",
    //       d: "x",
    //     },
    //   ],
    //   answer: "=",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 24,
    //   question: "What will the following code return: Boolean(10 &gt; 9)",
    //   options: [
    //     {
    //       a: "NaN",
    //       b: "false",
    //       c: "true",
    //     },
    //   ],
    //   answer: "true",
    //   score: 0,
    //   status: "",
    // },
    // {
    //   id: 25,
    //   question: "Is JavaScript case-sensitive?",
    //   options: [
    //     {
    //       a: "No",
    //       b: "Yes",
    //     },
    //   ],
    //   answer: "Yes",
    //   score: 0,
    //   status: "",
    // },
  ],
};
var quizApp = function () {
  this.score = 0;
  this.qno = 1;
  this.currentque = 0;
  var totalque = quiz.JS.length;
  this.displayQuiz = function (cque) {
    this.currentque = cque;
    if (this.currentque < totalque) {
      $("#tque").html(totalque);
      $("#previous").attr("disabled", false);
      $("#next").attr("disabled", false);
      $("#qid").html(quiz.JS[this.currentque].id + ".");
      $("#question").html(quiz.JS[this.currentque].question);
      $("#question-options").html("");
      for (var key in quiz.JS[this.currentque].options[0]) {
        if (quiz.JS[this.currentque].options[0].hasOwnProperty(key)) {
          $("#question-options").append(
            "<div class='form-check option-block'>" +
              "<label class='form-check-label'>" +
              "<input type='radio' class='form-check-input' name='option' id='q" +
              key +
              "' value='" +
              quiz.JS[this.currentque].options[0][key] +
              "'><span id='optionval'>" +
              quiz.JS[this.currentque].options[0][key] +
              "</span></label>"
          );
        }
      }
    }
    if (this.currentque <= 0) {
      $("#previous").attr("disabled", true);
    }
    if (this.currentque >= totalque) {
      $("#next").attr("disabled", true);
      for (var i = 0; i < totalque; i++) {
        this.score = this.score + quiz.JS[i].score;
      }
      return this.showResult(this.score);
    }
  };
  this.showResult = function (scr) {
    $("#result").addClass("result");
    $("#result").html(
      "<h1 class='res-header'>Total Score: &nbsp;" +
        scr +
        "/" +
        totalque +
        "</h1>"
    );
    for (var j = 0; j < totalque; j++) {
      var res;
      if (quiz.JS[j].score == 0) {
        res =
          '<span class="wrong">' +
          quiz.JS[j].score +
          '</span><i class="fa fa-remove c-wrong"></i>';
      } else {
        res =
          '<span class="correct">' +
          quiz.JS[j].score +
          '</span><i class="fa fa-check c-correct"></i>';
      }
      $("#result").append(
        '<div class="result-question"><span>Q ' +
          quiz.JS[j].id +
          "</span> &nbsp;" +
          quiz.JS[j].question +
          "</div>" +
          "<div><b>Correct answer:</b> &nbsp;" +
          quiz.JS[j].answer +
          "</div>" +
          '<div class="last-row"><b>Score:</b> &nbsp;' +
          res +
          "</div>"
      );
    }
  };
  this.checkAnswer = function (option) {
    var answer = quiz.JS[this.currentque].answer;
    option = option.replace(/</g, "&lt;"); //for <
    option = option.replace(/>/g, "&gt;"); //for >
    option = option.replace(/"/g, "&quot;");
    if (option == quiz.JS[this.currentque].answer) {
      if (quiz.JS[this.currentque].score == "") {
        quiz.JS[this.currentque].score = 1;
        quiz.JS[this.currentque].status = "correct";
      }
    } else {
      quiz.JS[this.currentque].status = "wrong";
    }
  };
  this.changeQuestion = function (cque) {
    this.currentque = this.currentque + cque;
    this.displayQuiz(this.currentque);
  };
};
var jsq = new quizApp();
var selectedopt;
$(document).ready(function () {
  jsq.displayQuiz(0);
  $("#question-options").on(
    "change",
    "input[type=radio][name=option]",
    function (e) {
      //var radio = $(this).find('input:radio');
      $(this).prop("checked", true);
      selectedopt = $(this).val();
    }
  );
});
$("#next").click(function (e) {
  e.preventDefault();
  if (selectedopt) {
    jsq.checkAnswer(selectedopt);
  }
  jsq.changeQuestion(1);
});
$("#previous").click(function (e) {
  e.preventDefault();
  if (selectedopt) {
    jsq.checkAnswer(selectedopt);
  }
  jsq.changeQuestion(-1);
});
