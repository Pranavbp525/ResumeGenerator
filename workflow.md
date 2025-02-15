```mermaid
graph TD
    subgraph UserInput
        A[User Resume]
        B[Job Description]
        C[Target Salary]
    end

    subgraph JDA
        D{{JDA CoreReq}} --> D1[JSON: core_req]
        E{{JDA CompanyValues}} --> E1[JSON: company_values]
        F{{JDA RelatedTerms}} --> F1[JSON: related_terms]
        G{{JDA JobDetails}} --> G1[JSON: job_details]
        H{{JDA Confidence}} --> H1[JSON: confidence]
    end

    B --> D
    B --> E
    B --> F
    B --> G
    B --> H

    subgraph RS
        I{{RS PhraseBonus}} --> I1[JSON: phrase_matches]
        J{{RS RoleComplexity}} --> J1[JSON: role_complexity]
        K{{RS RoleRelevance}} --> K1[JSON: role_relevance]
        L{{RS NearMiss}} --> L1[JSON: near_misses]
        M{{RS SectionScores}} --> M1[JSON: section_scores]
        N{{RS TotalScore}} --> N1[Float: total_score]
    end

    A --> I
    B --> I
    A --> J
    A --> K
    G1 --> K
    A --> L
    B --> L
    A --> M
    D1 --> M
    F1 --> M
    J1 --> M
    K1 --> M
    M --> N

    subgraph CO
        O{{CO KeywordInject}} --> O1[JSON: optimized_bullets]
        P{{CO Padding}} --> P1[JSON: optimized_bullets_padded]
    end

    A --> O
    M1 --> O
    D1 --> O
    F1 --> O
    L1 --> P
    A --> P
    O --> O1
    O --> P1


    subgraph FR
        Q{{FR KeywordRatio}} --> Q1[JSON: keyword_ratio]
        R{{FR MetricsCheck}} --> R1[JSON: metrics_check]
        S{{FR Dealbreaker}} --> S2[JSON: dealbreaker]
        T{{FR StyleCheck}} --> T1[JSON: style_check]
        U{{FR MetricsEst}} --> U1[JSON: optimized_bullets_metrics]
        V{{FR Assessment}} --> V1[JSON: final_assessment]
    end

    P1 --> Q
    O1 --> Q
    D1 --> Q
    F1 --> Q
    P1 --> R
    O1 --> R
    P1 --> S
    O1 --> S
    L1 --> S
    P1 --> T
    O1 --> T
    P1 --> U
    P1 --> V
    O1 --> V
    Q1 --> V
    R1 --> V
    S2 --> V
    T1 --> V
    U1 --> V

     subgraph SB
        W{{SB Salary}} --> W1[Revised Resume Text]
    end

    V1 --> W
    B --> W
    C --> W

    subgraph Output
        X[Templating Engine] --> Y[Resume PDF/DOCX]
    end

    V1 --> X
    W1 --> X

    linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43 stroke:#000,stroke-width:1px
    linkStyle 15,23,32,36,42 stroke:#f00,stroke-width:2px
