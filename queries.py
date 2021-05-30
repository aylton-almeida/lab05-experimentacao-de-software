def get_one_attributes():
    return """
        query {
              user(login: "torvalds") {
                login
                id
                avatarUrl
                url
                isSiteAdmin
                name
                company
                websiteUrl
                location
                email
                isHireable
                bio
                twitterUsername
                publicRepos: repositories(privacy:PUBLIC) {
                  totalCount
                }
                publicGists: gists(privacy: PUBLIC) {
                  totalCount
                }
                followers {
                  totalCount
                }
                following {
                  totalCount
                }
                createdAt
                updatedAt
              }
            }
  """


def get_one_name():
    return """
        query {
              user(login: "torvalds") {
                name
              }
        }
  """


def get_all_attributes():
    return """
        {
          search(type: USER, first: 100, query: "") {
            nodes {
              ... on User {
                login
                id
                avatarUrl
                url
                isSiteAdmin
                name
                company
                websiteUrl
                location
                email
                isHireable
                bio
                twitterUsername
                publicRepos: repositories(privacy: PUBLIC) {
                  totalCount
                }
                publicGists: gists(privacy: PUBLIC) {
                  totalCount
                }
                followers {
                  totalCount
                }
                following {
                  totalCount
                }
                createdAt
                updatedAt
              }
            }
          }
        }
  """


def get_all_name():
    return """
        {
          search(type: USER, first: 100, query: "") {
            nodes {
              ... on User {
                name
              }
            }
          }
        }
  """
