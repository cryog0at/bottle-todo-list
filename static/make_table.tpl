<!DOCTYPE html>
<html>

<head>
  <title>todo</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
  <p>here's what's happenin:</p>
  <table border="1">
  <h2>Stuff in Progress!</h2>
  %for row in activerows:
    <tr>
      %# id
      <td>{{row[0]}}</td>
      %# task
      <td>{{row[1]}}</td>
      <td><a href="/makedone/{{row[0]}}">Done</a></td> 
      <td><a href="/delete/{{row[0]}}">Delete</a></td>
    </tr>
  %end
  </table>
<br><br>
<table border="1">
  <h2>Stuff That's Done!</h2>
  %for row in donerows:
    <tr>
      %# id
      <td>{{row[0]}}</td> 
      %# task
      <td>{{row[1]}}</td> 
      <td><a href="/makeactive/{{row[0]}}">Active</a></td> 
      <td><a href="/delete/{{row[0]}}">Delete</a></td>
    </tr>
  %end
  </table>
  <br><br>
  <h3>What other stuff do you need to do?</h3>
  <form action="/addnew" method="post">
    <input type="text" name="newitem" placeholder="type some stuff in here">
    <br>
    <input type="radio" name="status" id="A" value="1" checked>
    <label for="A">Active</label>
    <input type="radio" name="status" id="D" value="0">
    <label for="D">Done</label>
    <br>
    <input type="submit" value="Submit!" >
  </form>
  <br><br>
  <h3>Edit an Item</h3>
  <form action="/updateitem" method="post">
    <input type="text" name="updatedtask" placeholder="type some stuff in here">
    <br>    
    <select name="rowid">
      %for id in rowids:
      <option value="{{id[0]}}">{{id[0]}}</option>
      %end
    </select>
    <br>
    <input type="submit" value="Update!">
  </form>
</body>

</html>
