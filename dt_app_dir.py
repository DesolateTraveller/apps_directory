    .version-badge a {
        color: #fff;
        text-decoration: none;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 4px;
        background: rgba(255,255,255,0.15);
        transition: background 0.2s;
    }
    .version-badge a:hover {
        background: rgba(255,255,255,0.3);
        text-decoration: underline;
    }
    .version-badge .email {
        opacity: 0.95;
        font-family: monospace;
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">🖥️ Apps Directory</div>
        <div class="version-badge">
            <span class="email">✉ avijit.mba18@gmail.com</span>
            <span style="opacity:0.7;">|</span>
            <a href="{pdf_view_link}" target="_blank">📄 View PDF</a>
        </div>
    </div>
    """.format(pdf_view_link=pdf_view_link),
    unsafe_allow_html=True
)
