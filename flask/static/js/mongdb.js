async function main(){
    /**
    * Connection URI. Update <username>, <password>, and <your-cluster-url> to reflect your cluster.
    * See https://docs.mongodb.com/ecosystem/drivers/node/ for more details
    */
    const uri = "mongodb://Jinsung:loverk2s%21@mongodb://3.37.202.252:27017/youtube_comment_database";
    const client = new MongoClient(uri);
  
    try {
      // Connect to the MongoDB cluster
      await client.connect();
  
      // Make the appropriate DB calls
      await  listDatabases(client);
    } catch (e) {
      console.error(e);
    } finally {
      await client.close();
    }
  }
  
  main().catch(console.error);