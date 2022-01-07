This is just a brief list of requirements.

# Functionality:

Pull data from the data service, and serve it to the strategy implementation team.

## Underlying Requirements

- A docker-compose file that runs this server and a MySQL / PostgreSQL database.
- An efficient, quick API puller. Preferably written in a lower level / faster language with concurrency.
    - Examples are C, C++, Go, Rust, Julia, etc.
- An exposed API, written in any convenient language, but preferably NodeJS
- An exposed database, in case I want to get the data myself
    - This is temporary and can be fixed later on.

# Preferred Roadmap

1. Design the API to pull the data from the data service.
2. Cleaning / Compressing and inserting this data into a database
3. A CD script that allows easy deployment
4. An exposed API that allows SI to get the data easily, without having to worry about database interactions.
    1. GraphQL is best for this

## API Requirements

### GraphQL Sample Request

- This sample request gets me data about AAPL stock from today, Jan 7th till Jan 1st, with a 5 minute interval.
    - I only want the close data so that maybe I can graph it.

```graphql
equity (name: "AAPL", 
	market: "NYSE", 
	timestep_start:1641599038, 
	timestep_end:1641109438, 
	resolution: "m",
	resolution_weight: 5
) {

datamembers {
	timestamp
	close
	volume
}
```

### Sample Response

```graphql
{
	timestamp: [1641109438, 1641109439, 1641109440]
	close: [111.55, 111.65, 111.75]
}
```

### GraphQL Schema

```graphql
type Equity {
	name: String
	market: String
  timestep_start: Int
  timestep_end: Int
  resolution: String
	resolution_weight: Int
	datamembers: {
		timestamp: [Int]
		high: [Float]
		low: [Float]
		close: [Float]
		open: [Float]
		volume: [Float]
	}
}
```
